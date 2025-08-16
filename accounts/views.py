from django.shortcuts import render
from django.http import HttpResponse

# 🟢 Temporary in-memory storage
users = []

def home(request):
    return render(request, "accounts/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # check if user exists
        for u in users:
            if u["username"] == username:
                return HttpResponse("❌ User already registered!")

        # add new user
        users.append({"username": username, "password": password})
        return HttpResponse("✅ Signup successful!")

    return HttpResponse("Method not allowed")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        for u in users:
            if u["username"] == username and u["password"] == password:
                return HttpResponse("🎉 Login successful!")

        return HttpResponse("❌ Invalid username or password!")

    return HttpResponse("Method not allowed")
