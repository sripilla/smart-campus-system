from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Student, Attendance, Marks


# 🔐 LOGIN VIEW
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')


# 🏠 DASHBOARD VIEW
@login_required
def dashboard(request):
    user = request.user

    student = None
    attendance = []
    marks = []
    attendance_percentage = 0
    total_classes = 0
    present_count = 0

    # If user is student → fetch related data
    if user.role == 'student':
        try:
            student = Student.objects.get(user=user)

            attendance = Attendance.objects.filter(student=student)
            marks = Marks.objects.filter(student=student)

            total_classes = attendance.count()
            present_count = attendance.filter(status=True).count()

            if total_classes > 0:
                attendance_percentage = (present_count / total_classes) * 100
            else:
                attendance_percentage = 0

        except Student.DoesNotExist:
            student = None

    context = {
        'user': user,
        'role': user.role,
        'student': student,
        'attendance': attendance,
        'marks': marks,
        'attendance_percentage': attendance_percentage,
        'total_classes': total_classes,
        'present_count': present_count
    }

    return render(request, 'dashboard.html', context)


# 👨‍🏫 MARK ATTENDANCE (FACULTY)
@login_required
def mark_attendance(request):

    # Restrict only faculty
    if request.user.role != 'faculty':
        return redirect('dashboard')

    students = Student.objects.all()

    if request.method == 'POST':
        student_id = request.POST.get('student')
        date = request.POST.get('date')
        status = request.POST.get('status')

        student = Student.objects.get(id=student_id)

        Attendance.objects.create(
            student=student,
            date=date,
            status=True if status == 'present' else False
        )

        return redirect('dashboard')

    return render(request, 'mark_attendance.html', {'students': students})