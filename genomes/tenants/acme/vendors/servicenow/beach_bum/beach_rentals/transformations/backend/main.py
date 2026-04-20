from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import router as beach_rental_router
from .agent import route_task, execute_workflow, get_history

app = FastAPI(
    title="Beach Bum Rentals API",
    description="API for managing beach rentals at Beach Bum",
    version="1.0.0"
)

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Lifespan events
@app.on_event("startup")
async def startup_event():
    print("Application startup logic here...")

@app.on_event("shutdown")
async def shutdown_event():
    print("Application shutdown logic here...")

# Include router
app.include_router(beach_rental_router)

# Agent endpoints
@app.post("/api/agent/execute")
async def execute_task_endpoint(task: str, payload: dict):
    result = await route_task(task, payload)
    return result

@app.post("/api/agent/workflow")
async def execute_workflow_endpoint(workflow: str, context: dict):
    result = await execute_workflow(workflow, context)
    return result

@app.get("/api/agent/history")
async def get_history_endpoint(limit: int = 10):
    return get_history(limit)