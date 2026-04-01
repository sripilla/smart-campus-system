# 🎓 Smart Campus Management System (Django + AI)

A web-based Smart Campus system built using Django that allows students, faculty, and admin to manage academic data with an integrated AI-based performance prediction feature.

---

## 🚀 Features

### 👩‍🎓 Student
- View attendance and marks
- See performance analytics
- AI-based performance prediction (Excellent / Average / At Risk)
- Visual charts (Bar + Pie)

### 👨‍🏫 Faculty
- Mark student attendance

### ⚙️ Admin
- Manage students, marks, and attendance via Django Admin Panel

### 🤖 AI Feature
- Predicts student performance based on:
  - Attendance %
  - Average marks
- Provides:
  - Smart insights
  - Warning alerts for low performance

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS
- **Charts:** Chart.js
- **Database:** SQLite (default)

---

## 📂 Project Structure
e
smart-campus-system/
│
├── smart_campus/
│ ├── models.py
│ ├── views.py
│ ├── ai_utils.py
│
├── core/
├── templates/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── data.json

---

## ⚙️ Setup Instructions (Run on New System)

### 1️⃣ Clone Repository
```bash
git clone https://github.com/sripilla/smart-campus-system.git
git@github.com:sripilla/smart-campus-system.git
cd smart-campus-system

2️⃣ Create Virtual Environment

python -m venv venv 

3️⃣ Activate Virtual Environment
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

4️⃣ Install Dependencies

pip install -r requirements.txt

5️⃣ Apply Migrations
python manage.py migrate

6️⃣ Load Data (Optional but Recommended - Test data)
python manage.py loaddata data.json

7️⃣ Run Server
python manage.py runserver

🌐 Open in Browser
http://127.0.0.1:8000/

🔐 Sample Login Credentials

| Username | Password  | Role    |
| -------- | --------- | ------- |
| student1 | Smart@123 | Student |
| student2 | Smart@123 | Student |
| student3 | Smart@123 | Student |

AI Logic (Simplified)

The system predicts performance using:

High Attendance + High Marks → Excellent
Medium values → Average
Low values → At Risk

This rule-based system can be extended into Machine Learning models.

Data Handling
Uses SQLite database (db.sqlite3)
Data is local by default
Can be exported/imported using:

python manage.py dumpdata > data.json
python manage.py loaddata data.json

Security Note

Passwords are securely stored using Django’s hashing system.
Always use:

set_password()
Django admin password forms

Future Enhancements
Machine Learning model integration
Student ranking system
Performance trend graphs
Chatbot assistant

Author
Likitha Sai Sri Pilla

Final Status

✅ Authentication system
✅ Role-based dashboard
✅ Data visualization
✅ AI prediction system
✅ Multi-user testing