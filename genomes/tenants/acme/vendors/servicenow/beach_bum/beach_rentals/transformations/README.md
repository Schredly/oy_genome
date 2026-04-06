# Beach Bum Rentals - Replit AI App

This application is a transformation of a ServiceNow application into a Replit AI application using FastAPI. It provides an API for managing beach rentals and implements business workflows for rental approvals.

## Features

- **API for Beach Rentals**: Create, read, update, and delete rental entries.
- **Business Logic**: Automated approval processes for rental requests.
- **Frontend**: Simple HTML/CSS frontend for interacting with the rental services.
- **Agent Integration**: Task and workflow execution with history tracking.

## Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run on Replit**:
   Ensure you have a Replit account and open the repository using Replit. The application is configured to run using the provided `.replit` and `replit.nix` configurations.

3. **Local Development**:
   If you prefer local development, ensure you have Python and the necessary packages installed. You can install dependencies with:
   ```bash
   pip install -r transformations/requirements.txt
   ```

4. **Start the Server**:
   Run the server using Uvicorn:
   ```bash
   uvicorn transformations.backend.main:app --host 0.0.0.0 --port 8080
   ```

5. **Access the Application**:
   Visit `http://localhost:8080` to interact with the API and the frontend interface.

## API Endpoints

- **Beach Rentals**:
  - `GET /api/beach_rentals`: List all rentals.
  - `GET /api/beach_rentals/{id}`: Retrieve a specific rental.
  - `POST /api/beach_rentals`: Create a new rental.
  - `PUT /api/beach_rentals/{id}`: Update an existing rental.
  - `DELETE /api/beach_rentals/{id}`: Delete a rental.

- **Agent**:
  - `POST /api/agent/execute`: Execute a specific task.
  - `POST /api/agent/workflow`: Execute a defined workflow.
  - `GET /api/agent/history`: Retrieve task execution history.

## Data Seeding

For demonstration purposes, an initial data seed is provided in `transformations/data/seed.json`.

## Customization

Feel free to extend and customize the application to fit your needs. The modular structure makes it easier to integrate additional features or connect to different data sources.

## License

This project is licensed under the MIT License.