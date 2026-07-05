# Career Connect

Career Connect is a Flask-based job portal web application where users can browse job openings, view job details, and submit applications online.

This project was built to practice Flask development with SQLAlchemy, WTForms, Jinja templates, and Bootstrap.

## Features

- View all available jobs
- View detailed information for each job
- Submit job applications
- Edit submitted applications
- Delete submitted applications with confirmation modal
- Flash messages for create, update, and delete actions
- Search jobs by title or location
- Sort jobs by title or location
- Pagination for the jobs list
- Field-level form validation errors
- Custom 404 and 500 error pages
- Shared navbar and footer using template inheritance

## Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- WTForms
- Jinja2
- Bootstrap 5
- SQLite

## Project Structure

```bash
career-connect/
│
├── app.py
├── database.py
├── forms.py
├── requirements.txt
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── jobpage.html
│   ├── application_submitted.html
│   ├── applications.html
│   ├── edit_application.html
│   ├── 404.html
│   └── 500.html
│
└── static/
    └── hammer.png
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/career-connect.git
cd career-connect
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows
```bash
venv\Scripts\activate
```

### Mac/Linux
```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python app.py
```

Then open:

```bash
http://127.0.0.1:5000/
```

## Demo Flow

1. Open the home page
2. Browse or search jobs
3. Open a job details page
4. Submit an application
5. View all submitted applications
6. Edit or delete an application
7. Test pagination, sorting, and error pages

## Learning Goals

This project was built to practice:

- Flask routing
- Template inheritance with Jinja
- Database models with SQLAlchemy
- Form validation using WTForms
- CRUD operations
- Search, sorting, and pagination
- Bootstrap UI integration
- Error handling and flash messaging

## Future Improvements

- User authentication
- Admin dashboard
- Resume file upload
- Better job filtering
- Deployment with Render
- Environment variable configuration for production

## Author

Built as a Flask learning and portfolio project.