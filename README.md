# Simple OAuth Django App

A quick and simple OAuth2 implementation for Django applications, designed to provide robust authentication and authorization mechanisms. This project integrates OAuth2 authentication using Django OAuth Toolkit.

## Description

This is a basic Django application that utilizes OAuth authentication through the Authorization Code method. The project, is designed to offer an uncomplicated OAuth2 system for Django applications, accommodating different OAuth2 grant types such as Authorization Code and Client Credentials. 

## Specifications

- **OAuth2 Authentication:** Implement OAuth2 flows including Authorization Code, Implicit, and Client Credentials.
- **Error Handling:** Centralized error handling with informative responses.

## Prerequisites

- Python (v3.8 or higher)
- Django (v3.2 or higher)
- Django OAuth Toolkit (v1.7 or higher)
- MySQL (or any other SQL database)
- Docker (for containerization)

## Technologies Used 

- **Django:** High-level Python web framework for rapid development.
- **Django OAuth Toolkit:** Django library for OAuth2 implementation.
- **Django REST Framework (DRF):** Toolkit for building Web APIs.
- **MySQL Connector/Python:** MySQL adapter for Python.
- **Docker:** Containerization of the application.
- **pytest:** Testing framework for unit and integration tests.

## Setup Installations Requirements

    * To set up and run the application locally, follow these steps:

    1. git clone https://github.com/YomZsamora/django-o-auth.git.
    2. Create a .env file in the app/ directory and add your environment variables.
    3. Install dependencies: `pip install -r requirements.txt`.
    4. Run database migrations: `python manage.py migrate`.
    5. Start the development server: `docker-compose up --build -d`.
    6. Navigate to http://localhost:8022/ in your browser or use Postman to interact with the API.

### Development

Want to contribute? Great! Here's how you can help:

- Fork the repo
- Create a new branch (git checkout -b feature-name)
- Make the appropriate changes in the codebase.
- Test your changes to ensure they work as expected.
- Commit your changes (git commit -m 'Add feature')
- Push to the branch (git push origin feature-name)
- Create a Pull Request explaining your changes.

### Running Tests

This project includes unit and integration tests to ensure the correctness of the codebase.

To run the tests:
```sh
docker-compose exec o-auth pytest
```
To run tests with coverage:
```sh
docker-compose exec o-auth pytest --cov=.
```

### Known Bugs

If you encounter any bugs or issues while using the application, please open an issue on the GitHub repository here. Be sure to include details of the issue and steps to reproduce it.

### License

*MIT License*

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
