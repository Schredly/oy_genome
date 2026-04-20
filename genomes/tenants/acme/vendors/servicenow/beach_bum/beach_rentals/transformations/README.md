# Beach Bum Rentals

Welcome to the Beach Bum Rentals API and Frontend application. This project allows you to manage beach equipment rentals through a FastAPI-based backend and a simple HTML/CSS frontend.

## Project Structure

- `backend/`: Contains the FastAPI application implementation.
  - `main.py`: The FastAPI entry point and configuration.
  - `routes.py`: Defines RESTful API endpoints for beach rentals.
  - `models.py`: Pydantic models representing the data structure.
  - `store.py`: In-memory data store for managing rentals.
  - `services/`: Business logic and workflows.
    - `logic.py`: Contains validation rules and business logic functions.
    - `workflows.py`: Implements workflows for rental approvals.

- `frontend/`: Simple HTML/CSS for user interfacing.
  - `index.html`: Main page displaying rental forms and data.
  - `style.css`: Styling for the frontend.

- `data/`: Contains seed data to initialize the rental store.
  - `seed.json`: Sample data for beach rentals.
  
- `requirements.txt`: Python package requirements.
- `.replit`: Replit configuration file.
- `replit.nix`: Replit environment setup.
  
## Requirements

- Python 3.11
- FastAPI
- Uvicorn
- Pydantic
- SQLAlchemy
- aioredis

## How to Run

1. **Install Dependencies**:
   Make sure you have Python 3.11 and the required packages installed. You can use the `replit.nix` file with Replit to set up the environment automatically.

2. **Start the Application**:
   Run the following command to start the backend server:
   ```
   uvicorn backend.main:app --host 0.0.0.0 --port 8080
   ```

3. **Access the Frontend**:
   Open `frontend/index.html` in your browser to interact with the application.

## Features

- **List Rentals**: View all active beach rentals.
- **Create Rentals**: Submit a form to create a new rental.
- **Manage Rentals**: Edit or delete existing rentals.
- **Workflow Automation**: Process approval workflows for rental requests.

## License

This project is licensed under the MIT License.