# Django ToDo App

This is a simple ToDo app built with Django, HTML, CSS, Bootstrap 5, jQuery, Ajax, and django-ajax-datatable. It includes authentication and utilizes Bootstrap modals for creating, updating, and viewing task details.

## Features
- Responsive website
- User authentication
- Single-page application design
- Bootstrap 5 for styling
- jQuery and Ajax for dynamic updates
- django-ajax-datatable for data table functionality
- SweetAlert for success and error messages
- Poetry for managing dependencies
- Conda environment setup
- Database migration using Django's `makemigrations` command

## Prerequisites

- Python 3.12
- Conda

## Getting Started
1. **Clone the repository**

```bash
git clone https://github.com/Rajeshkumar-14/django-todo-app.git
```

2. **Set up a Conda environment**

```bash
conda create --name todo-env python=3.12
conda activate todo-env
```

3. **Create .env file:**

   - Create a `.env` file in the main directory for mail sending purpose using [mailtrap.io](https://mailtrap.io/).

     ```env
     EMAIL_HOST=smtp.mailtrap.io
     EMAIL_PORT=2525
     EMAIL_HOST_USER=your_username
     EMAIL_HOST_PASSWORD=your_password
     ```

   - Remove spaces between the variable and equals and the value to avoid errors while copying from the website.

4. **Install Poetry**

```bash
pip install Poetry
```

5. **Install dependencies using Poetry**

```bash
poetry install
```

6. **Apply database migrations**

```bash
python manage.py makemigrations todo_app
python manage.py migrate
```

7. **Run the development server**

```bash
python manage.py runserver
```

Visit [localhost:8000](http://localhost:8000) or [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser to see the app.

## Usage
- Navigate to the app's homepage.
- Use the provided authentication system to log in or register.
- Add, update, and view tasks using the Bootstrap modals.
- SweetAlert will display success or error messages for each action.

## Contributing

- Contributions are welcome! If you have any suggestions, bug reports, or feature requests, feel free to open an issue or submit a pull request.

