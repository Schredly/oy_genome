from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import router as api_router

app = FastAPI(
    title="ACME Technical Catalog",
    description="A Technical Catalog application translated from ServiceNow to Replit using FastAPI.",
    version="1.0.0"
)

# Setup CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    # Setup or initialize any resources here
    print("Application startup")

@app.on_event("shutdown")
async def shutdown_event():
    # Tear down or clean up any resources here
    print("Application shutdown")

# Include API routes
app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)