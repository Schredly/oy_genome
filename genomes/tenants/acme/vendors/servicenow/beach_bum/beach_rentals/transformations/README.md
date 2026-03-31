# Beach Rentals API

This is a FastAPI-based application designed to manage beach rental operations, specifically focusing on tracking and managing update sets within the application lifecycle.

## Project Structure

- **backend/**: Contains the API and business logic.
  - `main.py`: Entry point of the application.
  - `routes.py`: Defines the API endpoints.
  - `models.py`: Pydantic models for data validation.
  - `store.py`: In-memory data storage.
  - `services/`: Contains business logic and workflows.
    - `logic.py`: Logic handling for update set state transitions.
    - `workflows.py`: Workflow definitions and executions.
    - `agent.py`: Agent with task routing and execution capabilities.

- **frontend/**: Static HTML and CSS files for a basic dashboard interface.
  - `index.html`: Dashboard for viewing and managing update sets.
  - `style.css`: Styles for the dashboard interface.

- **data/**: Contains initial data for the application.
  - `seed.json`: Seed data for update sets.

- **requirements.txt**: Python dependencies.
- **.replit**: Run configuration for Replit.
- **replit.nix**: Nix environment configuration file.

## Getting Started

1. **Install Dependencies**: Ensure you have Python 3.11 and the necessary dependencies installed. You can use the provided `replit.nix` file if using Replit.

2. **Run the Application**: Use Uvicorn to run the FastAPI application.
   ```
   uvicorn backend.main:app --host 0.0.0.0 --port 8080
   ```

3. **Access the Dashboard**: Open your web browser to `http://localhost:8080` to access the Beach Rentals dashboard.

## API Endpoints

- **GET /api/update_set**: Retrieve all update sets.
- **GET /api/update_set/{id}**: Retrieve a specific update set by ID.
- **POST /api/update_set**: Create a new update set.
- **PUT /api/update_set/{id}**: Update an existing update set.
- **DELETE /api/update_set/{id}**: Delete an update set by ID.

## Workflow Execution

- **POST /api/agent/execute**: Execute a specific task with a given payload.
- **POST /api/agent/workflow**: Run a predefined workflow with context data.
- **GET /api/agent/history**: Retrieve the history of executed tasks.

## License

This project is developed for educational purposes and is not intended for production use. Please review and customize for your specific use case as needed.