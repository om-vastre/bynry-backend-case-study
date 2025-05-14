# Gas Utility Service Management System

A Django-based web application for managing gas utility service requests and customer support. This system allows customers to submit service requests, track their status, and manage their account information.

## Features

### Customer Features
- User registration and authentication
- Profile management with contact information
- Service request submission with file attachments
- Real-time request status tracking
- Request history and details view

### Service Request Management
- Create new service requests
- Upload supporting documents
- Track request status (Pending, In Progress, Resolved)
- View request history
- Update request status

### User Interface
- Responsive design using Bootstrap 5
- Intuitive navigation
- Mobile-friendly interface
- Clean and modern UI

## Technical Stack

- Python 3.11.0
- Django 5.0.2
- Bootstrap 5.3.0
- SQLite (Development)
- Pillow (Image processing)

## Project Structure

```
gas_utility_service/
├── manage.py
├── requirements.txt
├── gas_utility_service/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── accounts/
│   │   ├── models.py      # User profile management
│   │   ├── views.py       # Authentication views
│   │   ├── forms.py       # User forms
│   │   └── urls.py        # Account URLs
│   ├── service_requests/
│   │   ├── models.py      # Service request models
│   │   ├── views.py       # Request handling views
│   │   ├── forms.py       # Request forms
│   │   └── urls.py        # Request URLs
│   └── dashboard/
│       ├── models.py
│       ├── views.py
│       └── urls.py
├── templates/
│   ├── base.html          # Base template
│   ├── accounts/          # Account templates
│   └── service_requests/  # Request templates
├── static/                # Static files
└── media/                 # User uploaded files
```

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd gas_utility_service
```

2. Create and activate virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Unix/MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run development server:
```bash
python manage.py runserver
```

## Usage

1. Access the application at `http://127.0.0.1:8000/`
2. Register a new account or login with existing credentials
3. Create and manage service requests
4. Track request status and updates

## Admin Interface

Access the admin interface at `http://127.0.0.1:8000/admin/` to:
- Manage user accounts
- Monitor service requests
- Update request statuses
- Handle user profiles

## API Endpoints

- `/accounts/register/` - User registration
- `/accounts/login/` - User login
- `/accounts/logout/` - User logout
- `/accounts/profile/` - User profile management
- `/service-requests/create/` - Create new service request
- `/service-requests/list/` - View all service requests
- `/service-requests/detail/<id>/` - View request details

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the repository or contact the development team. 