import mysql.connector
from django.db import models
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse

# Establish a connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="password",  # Replace with your MySQL password
    database="testdb"
)

# Check if the connection is successful
if connection.is_connected():
    print("Connected to MySQL database")

class Member(models.Model):
    apartment_city = models.CharField(max_length=255)
    price_of_apartment = models.IntegerField()
    rooms_in_apartment = models.CharField(max_length=255)

    def create_apartment(apartment_city, price_of_apartment, rooms_in_apartment):
        cursor = connection.cursor()
        query = """
        INSERT INTO users (apartment_city, price_of_apartment, rooms_in_apartment) VALUES (%s, %s, %s)
        """
        cursor.execute(query, (apartment_city, price_of_apartment, rooms_in_apartment))
        connection.commit()
        print(f"User {apartment_city} added successfully.")

    # Read Operation    
    def read_users():
        cursor = connection.cursor()
        query = "SELECT * FROM users"
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)

    # Filter By Price and sorted Operation     
    def filter_by_price(price1, price2):
        cursor = connection.cursor()
        query = """
        SELECT apartment_city, price_of_apartment, rooms_in_apartment 
        FROM DekhoFlat 
        WHERE price_of_apartment >= %s AND price_of_apartment <= %s 
        ORDER BY price_of_apartment ASC
        """
        cursor.execute(query, (price1, price2))
        for row in cursor.fetchall():
            print(row)

    # Filter By Alphabetically orders
    def filter_by_alphabets(alphabets):
        cursor = connection.cursor()
        query = """
        SELECT apartment_city, price_of_apartment, rooms_in_apartment 
        FROM DekhoFlat 
        WHERE apartment_city LIKE %s 
        ORDER BY price_of_apartment ASC
        """
        cursor.execute(query, (f"{alphabets}%",))
        for row in cursor.fetchall():
            print(row)

    # Update Operation
    def update_apartment(user_id, apartment_city=None, price_of_apartment=None, rooms_in_apartment=None):
        cursor = connection.cursor()
        updates = []
        if apartment_city:
            updates.append(f"apartment_city = '{apartment_city}'")
        if price_of_apartment:
            updates.append(f"price_of_apartment = {price_of_apartment}")
        if rooms_in_apartment:
            updates.append(f"rooms_in_apartment = '{rooms_in_apartment}'")

        if updates:
            query = f"UPDATE users SET {', '.join(updates)} WHERE id = %s"
            cursor.execute(query, (user_id,))
            connection.commit()
            print(f"Flat with ID {user_id} updated successfully.")

    # Delete Operation        
    def delete_apartment(user_id):
        cursor = connection.cursor()
        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        connection.commit()
        print(f"User with ID {user_id} deleted successfully.")

    # Infinite Scrolling
    def my_view(request):
        items = Member.objects.all()  # Replace MyModel with your model
        page_number = request.GET.get('page', 1)
        paginator = Paginator(items, 10)  # Show 10 items per page
        page = paginator.get_page(page_number)
        if request.headers.get('HX-Request') == 'true':
            return render(request, 'my_partial_template.html', {'items': page.object_list, 'has_next': page.has_next()})
        else:
            return render(request, 'my_template.html', {'items': page.object_list, 'has_next': page.has_next()})
