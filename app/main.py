from fastapi import FastAPI
from app.routes import router

# Create FastAPI application
app = FastAPI(
    title="Spotify Feature Search API",
    description="A simple FastAPI application",
    version="1.0.0"
)

# Include routes
app.include_router(router, prefix="/api/v1")

@app.get("/")
async def root():
    """Root path endpoint"""
    return {"message": "Welcome to Spotify Feature Search API"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    """Get item endpoint"""
    return {"item_id": item_id, "q": q}