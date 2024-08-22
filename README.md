# Document Tracking System

## Project Overview

The **Document Tracking System** is a web-based application built using Django that allows departments to manage and track the progress of various documents. This system provides a user-friendly interface for tracking document statuses, viewing details, and managing documents within an organization.

## Features

- **User Authentication**: Secure login functionality for users to access the system.
- **Department Dashboard**: A department-specific dashboard that displays all documents related to that department along with their statuses.
- **Super Admin Dashboard**: A dashboard for super admins to monitor and track the status of documents across all departments.
- **Document Tracking**: Ability to track the progress and status of each document through the workflow.
- **Document Viewing**: Access and view documents directly from the system.
- **Visual Status Representation**: Pie charts to visually represent the status distribution of documents (e.g., Approved, Pending, Rejected, Transit).

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript (Chart.js)
- **Database**: MySQL
- **Version Control**: Git

## Installation

### Prerequisites

- Python 3.x
- Django 4.x
- MySQL

### Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/document-tracking-system.git
   cd document-tracking-system
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**
   - Ensure MySQL is installed and running.
   - Create a database named `file_management`.
   - Update the database credentials in the `settings.py` file under `DATABASES`.

5. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**
   - Open your web browser and go to `http://127.0.0.1:8000/login/`.

## Project Structure

- **Login_Page**: Handles user authentication and login.
- **Depart_Dashboard**: Manages and displays the department-specific dashboard.
- **Super_Dashboard**: Provides the super admin view for tracking documents across all departments.
- **Document_Details**: Manages and displays document details and tracking information.

## Usage

### Login

- Use your `Officer ID` and `Password` to log in.
- Depending on the ID, you will be redirected to either the Department Dashboard or the Super Admin Dashboard.

### Department Dashboard

- View all documents related to your department.
- Track the status and progress of each document.
- Click on `Track` to view detailed tracking information for a document.
- Click on `View` to access the document.

### Super Admin Dashboard

- Monitor document status across all departments.
- Visualize document status distribution using the pie chart.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes.
   ```bash
   git commit -m "Description of your changes"
   ```
4. Push to your branch.
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.


## Contact

For any questions or suggestions, please feel free to contact [krrishjaiswaljk8299@gmail.com].

---

