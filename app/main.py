"""FastAPI application for Makers Tech ChatBot.

This module contains the main FastAPI application instance and its configurations.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Makers Tech ChatBot",
    description=(
        "A ChatBot for Makers Tech e-commerce providing real-time "
        "inventory updates and product information"
    ),
    version="0.1.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Return a welcome message for the API root endpoint.

    Returns:
        dict: A dictionary containing the welcome message.
    """
    return {"message": "Welcome to Makers Tech ChatBot API"}
