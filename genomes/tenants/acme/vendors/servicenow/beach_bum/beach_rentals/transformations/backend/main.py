from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import router as api_router

app = FastAPI()

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Include the API router
app.include_router(api_router)

@app.on_event("startup")
async def startup_event():
    # Initialize application state, database connection pools, etc.
    pass

@app.on_event("shutdown")
async def shutdown_event():
    # Clean up resources, close database connections, etc.
    pass

@app.get("/")
async def root():
    return {"message": "Welcome to the Beach Rentals API"}