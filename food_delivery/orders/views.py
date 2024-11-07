# orders/views.py

from django.shortcuts import render, HttpResponse
from django.db import connection
# orders/views.py

def create_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')

        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Users (Name, Email, Password, Phone) VALUES (%s, %s, %s, %s)",
                [name, email, password, phone]
            )
        return HttpResponse("User created successfully!")
    
    return render(request, 'create_user.html')  # Render a form for user creation

def get_restaurants(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Restaurants")
        restaurants = cursor.fetchall()
    
    return render(request, 'restaurant_list.html', {'restaurants': restaurants})

