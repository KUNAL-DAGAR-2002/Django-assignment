# Django Project Readme

## Description
This Django project is a simple web application that manages customer information and their orders. It includes two models - Customer and Orders, along with features to display various statistics and provide date-wise filtering.

## Models

### 1. Customer
- **Fields:**
  - `name` - The name of the customer.
  - `number` - The customer's contact number.
  - `email` - The customer's email address.

### 2. Orders
- **Fields:**
  - `id` - The unique identifier for each order.
  - `value` - The monetary value of the order.
  - `customer` - A foreign key referencing the Customer model.
  - `date` - The date when the order was placed.

## Web App Features
The web app provides the following statistics on the home page:
- Total Orders
- Total Unique Customers
- Average Order Value
- Total Order Value

Additionally, the web app supports date-wise filtering.

## Admin Panel
The project includes the Django admin panel for easy management of data. You can access the admin panel using the following credentials:
- **Username:** admin
- **Password:** admin

## Run/start app
python manage.py runserver


## home
Contains all information about view, apps and models.

## Acess the app at
http://localhost:8000/

## Acess the admin at
http://localhost:8000/admin/
