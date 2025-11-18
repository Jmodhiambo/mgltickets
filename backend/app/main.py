from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.logging_config import configure_logging, logger
from core.logging_middleware import LoggingMiddleware

configure_logging() # Initialize logging configuration

app = FastAPI()

# Middlewares
# Add logging middleware
app.add_middleware(LoggingMiddleware)

# Mount Static Files
# Static files for serving uploaded event flyers
app.mount("/uploads", StaticFiles(directory="app/uploads"), name="uploads")

# Routes

# Register handlers globally