# B2B Web Application for Tunisian Post

This repository contains the implementation of a B2B web application developed during a final-year project at the Tunisian Post. The project focuses on improving the procurement process by facilitating communication and transactions between the Tunisian Post and its suppliers.

## Features

- **User Roles**:
  - **Administrator**: Manage product listings, modify and delete announcements, review supplier bids, and finalize procurement.
  - **Supplier**: Register on the platform, submit bids, and upload product sheets.
- **Core Functionalities**:
  - User authentication and registration.
  - Add, update, and delete product announcements.
  - Submit and review supplier bids.
  - Intuitive and user-friendly interfaces.

## Technologies Used

- **Frontend**:
  - HTML5, CSS, Bootstrap for styling and layout.
  - JavaScript for interactivity.

- **Backend**:
  - Python with Django framework for server-side logic and database interaction.

- **Tools**:
  - Visual Studio Code for development.
  - TablePlus for database management.

## How to Run

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt

3. Apply migrations:
   ```bash
   python manage.py migrate

4. Run the development server:
   ```bash
   python manage.py runserver

5. Access the application at http://127.0.0.1:8000.

