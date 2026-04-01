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

    # 🔥 Analytics variables
    attendance_percentage = 0
    total_classes = 0
    present_count = 0
    total_marks = 0
    average_marks = 0
    subject_count = 0

    # 🔥 Graph variables
    subjects = []
    scores = []
    absent_count = 0

    # ✅ STUDENT VIEW
    if user.role == 'student':
        try:
            student = Student.objects.get(user=user)

            attendance = Attendance.objects.filter(student=student)
            marks = Marks.objects.filter(student=student)

            # 📊 Attendance Calculation
            total_classes = attendance.count()
            present_count = attendance.filter(status=True).count()

            if total_classes > 0:
                attendance_percentage = (present_count / total_classes) * 100

            absent_count = total_classes - present_count

            # 📊 Marks Calculation
            total_marks = sum([m.marks for m in marks])
            subject_count = marks.count()

            if subject_count > 0:
                average_marks = total_marks / subject_count

            # 📊 GRAPH DATA
            subjects = [m.subject for m in marks]
            scores = [m.marks for m in marks]

        except Student.DoesNotExist:
            student = None

    # ✅ FACULTY VIEW
    elif user.role == 'faculty':
        attendance = Attendance.objects.all()
        marks = Marks.objects.all()

    # ✅ ADMIN VIEW
    elif user.role == 'admin':
        attendance = Attendance.objects.all()
        marks = Marks.objects.all()

    context = {
        'user': user,
        'role': user.role,
        'student': student,
        'attendance': attendance,
        'marks': marks,

        # 📊 Analytics
        'attendance_percentage': round(attendance_percentage, 2),
        'total_classes': total_classes,
        'present_count': present_count,
        'average_marks': round(average_marks, 2),
        'total_marks': total_marks,
        'subject_count': subject_count,

        # 🔥 GRAPH DATA
        'subjects': subjects,
        'scores': scores,
        'present_count': present_count,
        'absent_count': absent_count,
    }

    return render(request, 'dashboard.html', context)


# 👨‍🏫 MARK ATTENDANCE (FACULTY)
@login_required
def mark_attendance(request):

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