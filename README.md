# Second-Hand Clothes Marketplace

## Overview
This project is a Django-based REST API for a second-hand clothes marketplace. It allows users to list, search, publish, update, and delete garments. The API includes user authentication via JWT to ensure secure and personalized interactions.

## Features
- **User Authentication**: Secure login using JSON Web Tokens (JWT).
- **Garment Management**: 
  - **CRUD operations**: Create, retrieve, update, and delete garments.
  - **Search functionality**: Query garments based on type, size, price, and other attributes.
- **Publisher Validation**: Users can only update or delete garments they have published.
- **Custom User Model**: Includes full name and address fields.

## Requirements
- **Language**: Python
- **Framework**: Django and Django REST Framework
- **Database**: The default database is SQLite. If you wish to use a different database, create a `.env` file in the project’s root directory and specify the database configuration as shown below ex. (PostgreSQL):

  ```
  DB_ENGINE=django.db.backends.postgresql
  DB_NAME=my_database
  DB_USER=my_user
  DB_PASSWORD=my_password
  DB_HOST=localhost
  DB_PORT=5432

## Installation Instructions

### 1. Clone the Repository
Clone the project to your local machine and navigate to the project directory:
```bash
   git clone https://github.com/JuxhinMurthi/webz.git
   cd marketplace
```

### 2. Set Up the Virtual Environment
Create and activate a Python virtual environment:
```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies
Install the required Python packages:
```bash
   pip install -r requirements.txt
```

### 4. Configure the Database
The project uses **SQLite** by default. If you wish to use another database (e.g., PostgreSQL, MySQL), update the `DATABASES` setting in `settings.py` according to [Django's database documentation](https://docs.djangoproject.com/en/4.2/ref/settings/#databases).

### 5. Apply Migrations
Create and apply migrations to set up the database schema:
```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
```

### 6. Create a Superuser
Create an admin account to manage the application:
```bash
   python3 manage.py createsuperuser
```

### 7. Run Tests
Verify that the system is functioning correctly by running the test suite:
```bash
   python3 manage.py test
```

### 8. Start the Development Server
Launch the application locally:
```bash
   python3 manage.py runserver
```

Access the API at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Endpoints

### Authentication
- **Authenticate**: `/auth/token/` (POST)  
  Requires username and password.  
  Returns a JWT for authenticated access and refresh token.
- **Refresh token**: `/auth/token/refresh/` (POST)  
  Requires refresh token.  
  Returns a JWT for authenticated access.


### Garments (Public Access)
- **List Garments**: `/api/clothes/` (GET)  
  Searchable by `type`, `size`, `price`, etc.

- **Retrieve Garment**: `/api/clothes/<id>/` (GET)  
  Retrieves details of a specific garment.

### Garments (Authenticated Access)
- **Publish Garment**: `/api/clothes/publish/` (POST)  
  Requires `description`, `price`, `type`, and `size`.

- **Update Garment**: `/api/clothes/<id>/update/` (PUT)  
  Users can update only their own garments.

- **Delete Garment**: `/api/clothes/<id>/delete/` (DELETE)  
  Users can delete only their own garments.

---

## Models

### User
A custom user model that extends Django's `AbstractUser`:
- `full_name` (string, auto-generated from first and last name)
- `address` (string, optional)

### Garment
- `type` (selection, e.g., SH - Shirt, PA - Pants, JA - Jacket, TS - TShirt, SK - Skirt, DR - Dress, OT - Other)
- `description` (text)
- `size` (selection, e.g., SM - Small, MD - Medium, LG - Large)
- `price` (decimal)
- `publisher` (foreign key to the custom user model)

---

## Additional Resources
- [Django Documentation](https://docs.djangoproject.com/en/4.2/)
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
