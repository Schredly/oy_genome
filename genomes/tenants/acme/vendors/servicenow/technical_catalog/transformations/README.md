# ACME Technical Catalog

This is a Replit-native implementation of the ACME Technical Catalog application, originally derived from a ServiceNow application. The application provides services and resources that can be requested via a simple API and frontend interface.

## Features

- **Server Reboot Management**: Schedule and manage server reboot requests.
- **Database Restoration**: Request restores of databases from specific backups.
- **Beach Equipment Rental**: Rent beach equipment such as surfboards and beach chairs.
- **Knowledge Base Requests**: Request the creation of new knowledge bases for organizational use.
- **Application Server Provisioning**: Provision standard and large application servers.
- **Database Server and Oracle License Management**: Request database servers and related Oracle licenses.
- **Email Account Management**: Manage email account requests, including account creation and special configurations.

## Technology Stack

- **Python 3.11**: Main programming language.
- **FastAPI**: Web framework for building APIs.
- **Uvicorn**: ASGI server for running FastAPI applications.
- **Pydantic**: Data validation and settings management using Python type annotations.

## Directory Structure

- **backend/**: Contains all server-side code, including API routes, models, and business logic.
- **frontend/**: Contains HTML and CSS files for the client interface.
- **data/**: Contains seed data for the application.
- **transformations/**: Directory containing the transformed components of the application.

## Running the Application

To run the application on Replit:

1. Open the `.replit` file to ensure the correct entrypoint and command are set.
2. Use the built-in run command to start the application.
3. Access the application on the provided Replit URL.

## API Endpoints

Explore the RESTful API through the various endpoints defined in the `backend/routes.py` file. Here are a few examples:

- `/api/server-reboot` - Manage server reboot requests.
- `/api/database-restore` - Handle database restore requests.
- `/api/beach-equipment-rental` - Process rentals for beach equipment.
- `/api/request-knowledge-base` - Submit requests for new knowledge bases.

Refer to the file for a full list of available endpoints.

## Contributing

Contributions are welcome! Please fork this repository and create a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes necessary tests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.