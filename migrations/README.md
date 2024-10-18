# MarketPlace Flask Application

This is a marketplace web application built using **Flask**, **SQLAlchemy**, and **WTForms**. The application allows users to register, log in, buy, and sell items, providing basic e-commerce functionalities.

## Features

- **User Registration and Authentication:**
  - Secure user registration and login using Flask-Login and Flask-Bcrypt.
  - Form validation using WTForms with custom validation for unique usernames and email addresses.

- **Item Management:**
  - Users can purchase items available in the marketplace.
  - Users can sell items that they own.
  - Each user has a budget to manage their purchases.

- **Database Management:**
  - Models for `User` and `Item` entities.
  - Relationship between users and items.
  - Transactions update both the user's budget and the item's owner.

## Technology Stack

- **Backend:** Flask (Python)
- **Database:** SQLAlchemy with SQLite (can be configured for other databases)
- **Forms:** Flask-WTF for form handling
- **Password Hashing:** Flask-Bcrypt for secure password storage
- **User Authentication:** Flask-Login for managing user sessions
- **Database Migration:** Flask-Migrate for database versioning

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/marketplace-flask.git
   cd marketplace-flask
