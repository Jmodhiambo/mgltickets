#!/usr/bin/env python3
"""FastAPI entrypoint for MGLTickets."""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.core.logging_config import configure_logging, logger
from app.core.logging_middleware import LoggingMiddleware
from app.api.routes import auth, events

configure_logging() # Initialize logging configuration

app = FastAPI()

# Middlewares
# Add logging middleware
app.add_middleware(LoggingMiddleware)

# Mount Static Files
# Static files for serving uploaded event flyers
app.mount("/uploads", StaticFiles(directory="app/uploads"), name="uploads")

# Routes
app.include_router(auth.router, prefix="/api/v1", tags=["Authentication"])
app.include_router(events.router, prefix="/api/v1", tags=["Events"])

# Register handlers globally