Django Login/Signup App

This is a beginner-friendly Django project where users can sign up and log in.
The project uses Django’s default SQLite database, and it is also configured for Render Deployment (free cloud hosting).

📌 Features

User Signup & Login (with validation)

In-memory user store (for demo purposes)

Static files support (CSS/JS)

Ready for deployment on Render

Beginner-friendly setup

📂 Project Structure
login_django/
│── accounts/               # App (login & signup)
│   ├── templates/accounts/ # HTML templates
│   ├── static/accounts/    # CSS/JS files
│   ├── views.py            # Business logic
│   ├── urls.py             # App URLs
│── core/                   # Main Django project
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│── manage.py
│── requirements.txt
│── Procfile

⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/your-username/login_django.git
cd login_django

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate     # Windows
# OR
source venv/bin/activate  # Mac/Linux

3. Install Dependencies

Create requirements.txt with:

Django>=5.0,<6.0
gunicorn
whitenoise
psycopg2-binary
requests


Then install:

pip install -r requirements.txt

4. Run Initial Setup
python manage.py migrate

5. Run Development Server
python manage.py runserver


Visit: http://127.0.0.1:8000/signup

📝 Code Overview
accounts/views.py

Handles signup and login:

from django.shortcuts import render, redirect
from django.contrib import messages

users = {}  # temporary in-memory storage

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if username in users:
            messages.error(request, "User already exists!")
        else:
            users[username] = password
            messages.success(request, "Signup successful!")
            return redirect("login")

    return render(request, "accounts/signup.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if users.get(username) == password:
            messages.success(request, f"Welcome {username}!")
        else:
            messages.error(request, "Invalid credentials!")

    return render(request, "accounts/login.html")

🎨 Static Files (CSS)

Add CSS file: accounts/static/accounts/style.css

body {
  font-family: Arial, sans-serif;
  background: #f4f4f4;
  text-align: center;
}


Update core/settings.py

STATIC_URL = 'static/'
STATICFILES_DIRS = [ BASE_DIR / "accounts/static" ]
STATIC_ROOT = BASE_DIR / "staticfiles"


Collect Static Files

python manage.py collectstatic --noinput

🚀 Deployment on Render
1. Push Code to GitHub
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/your-username/login_django.git
git push -u origin main

2. Add Procfile

Create a file named Procfile in the root directory:

web: gunicorn core.wsgi:application

3. Deploy to Render

Go to https://render.com

Create New Web Service

Connect GitHub repo

Configure:

Build Command:

pip install -r requirements.txt && python manage.py collectstatic --noinput


Start Command:

gunicorn core.wsgi:application

4. Done 🎉

Your project will be live at:

https://your-app.onrender.com

👩‍💻 Author

Sonnya Varshney
