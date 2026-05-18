📌 Smart Job Portal (Django Project)
🚀 Project Overview

Smart Job Portal is a full-stack web application built using Django. It allows users to register, login, browse jobs, search jobs, view job details, and apply for jobs. Admins/recruiters can manage job listings using full CRUD operations.

✨ Features
🔐 User Authentication (Login / Register / Logout)
🧾 Add, View, Update, Delete Jobs (CRUD)
🔍 Job Search Functionality
📄 Job Detail Page
📩 Job Application System
🎨 Responsive UI using Bootstrap
👤 Session-based login system
🛠️ Tech Stack
Backend: Django (Python)
Frontend: HTML, CSS, Bootstrap
Database: SQLite
Version Control: Git & GitHub
📁 Project Structure
jobportal/
│
├── jobportal/        # Main project settings
├── portal/           # App (views, models, urls)
├── templates/        # HTML templates
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── add_job.html
│   ├── edit_job.html
│   ├── job_detail.html
│   └── success.html
├── db.sqlite3
└── manage.py
⚙️ How to Run Project
1️⃣ Clone Repository
git clone https://github.com/your-username/smart-job-portal.git
cd smart-job-portal
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Requirements
pip install django
4️⃣ Run Server
python manage.py runserver
🌐 Features Flow
User registers/login
User views available jobs
User searches jobs
User clicks job → job details page
User applies for job
Admin/recruiter can:
Add job
Edit job
Delete job
📌 Future Improvements
Recruiter dashboard
Resume upload feature
Email notification on application
Pagination for jobs
Deployment on cloud (Render / PythonAnywhere)
👨‍💻 Author

Hemanth Kumar
📍 India
💼 Django Full Stack Developer (Fresher)

⭐ Output

👉 A complete Django-based Job Portal with authentication + CRUD + search functionality.
