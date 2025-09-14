from fastapi import FastAPI
from app.routes import router
import os
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    yield
    # Shutdown
    # Close any open sessions
    if hasattr(app.state, 'spotify_service'):
        await app.state.spotify_service.close()

# Create FastAPI application
app = FastAPI(
    title="Spotify Feature Search API",
    description="A simple FastAPI application",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://www.joshchau.dev",
        "http://localhost:3000",
        "https://personal-website-client-beta.vercel.app",
        "https://vercel.com"
    ],  
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
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