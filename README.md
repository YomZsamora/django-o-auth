# Simple OAuth Django App

A quick and simple OAuth2 implementation for Django applications, designed to provide robust authentication and authorization mechanisms. 

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
- **google-auth:** Google Authentication library.
- **Django REST Framework (DRF):** Toolkit for building Web APIs.
- **MySQL Connector/Python:** MySQL adapter for Python.
- **Docker:** Containerization of the application.
- **CacheControl:** Cache-control adapter for requests library.
- **Faker:** Library for generating fake data.
- **pytest:** Testing framework for unit and integration tests.

## Obtaining Google Client ID and Client Secret

1. **Go to the Google Cloud Console**.
2. **Create a New Project**.
3. **Enable the OAuth Consent Screen**: Set up required fields like `App name`, `Support email`, etc.
4. **Create OAuth Credentials**:
    - Choose `Web application`.
    - Add redirect URI (`http://localhost:8022/v1/auth/oauth2callback`).
5. Copy the **Client ID** and **Client Secret** for use in the next step.

## Docker Compose Setup

This project supports Docker containerization for easy deployment. To run the application using Docker Compose, follow these steps:

1. Make sure you have Docker installed on your machine.
2. Create a `.env` file in the root directory and add the necessary environment variables.
    ```sh
    # Database settings
    - `MYSQL_ENGINE`: MySQL engine type (mysql.connector.django).
    - `MYSQL_DATABASE`: Main database name for the application.
    - `MYSQL_USER`: MySQL username for accessing the databases.
    - `MYSQL_PASSWORD`: Password for the MySQL user.
    - `MYSQL_ROOT_PASSWORD`: Root password for MySQL.
    - `MYSQL_HOST`: Hostname where MySQL is running - the database container (o-auth-db).
    - `MYSQL_PORT`: Port on which MySQL is listening (default is 3306).

    # Google OAuth Settings
    - `GOOGLE_TOKEN_URL`: URL to obtain an OAuth token from Google 'https://oauth2.googleapis.com/token'.
    - `GOOGLE_CLIENT_ID`: Client ID for OAuth authentication.
    - `GOOGLE_CLIENT_SECRET`: Client Secret for OAuth authentication.
    - `GOOGLE_REDIRECT_URI`: Redirect URI for OAuth callbacks 'http://localhost:8022/v1/auth/oauth2callback'.
    - `GOOGLE_GRANT_TYPE`: OAuth grant type, such as 'authorization_code'.
    - `GOOGLE_USER_INFO_URL`: 'https://www.googleapis.com/oauth2/v1/userinfo?alt=json'
    ```
3. Build and start the containers using Docker Compose:
    ```sh
    docker-compose up --build -d
    ```
4. The application should now be running inside a Docker container.
5. Access the API at http://localhost:8022/ or use Postman for interactions.

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
