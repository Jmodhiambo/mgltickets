#!/usr/bin/env python3
"""Events routes for MGLTickets."""

from fastapi import APIRouter, Depends
from app.schemas.event import EventOut
import app.services.event_services as event_services
from app.core.security import get_current_user

router = APIRouter()

@router.get("/events", response_model=list[EventOut])
async def get_all_events(user=Depends(get_current_user)):
    """
    Get all events.
    """
    return event_services.get_all_events_service()

@router.get("/events/test", response_model=list[EventOut])
async def get_latest_events(): # user=Depends(get_current_user)
    """
    Test the route.
    """
    return [
        {
            "id": 1,
            "title": "Exciting Music Festival Tonight",
            "organizer_id": 42,
            "description": "A fantastic show with live bands and food trucks.",
            "venue": "123 Main Street, Springfield",
            "start_time": "2025-11-21T18:00:00",
            "end_time": "2025-11-21T21:00:00",
            "flyer_url": "http://example.com/flyer1.png",
            "status": "active",
            "created_at": "2025-10-21T14:30:00",
            "updated_at": "2025-11-21T12:00:00"
        }
    ]


@router.get("/events/{event_id}", response_model=EventOut)
async def get_event_by_id(event_id: int, user=Depends(get_current_user)):
    """
    Get an event by its ID.
    """
    return event_services.get_event_by_id_service(event_id)

@router.post("/events", response_model=EventOut)
async def create_event(event_data: EventOut, user=Depends(get_current_user)):
    """
    Create a new event.
    """
    return event_services.create_event_service(event_data)

@router.put("/events/{event_id}", response_model=EventOut)
async def update_event(event_id: int, event_data: EventOut, user=Depends(get_current_user)):
    """
    Update an event by its ID.
    """
    return event_services.update_event_service(event_id, event_data)

@router.post("/events/{event_id}/approve", response_model=EventOut)
async def approve_event(event_id: int, user=Depends(get_current_user)):
    """
    Approve an event by its ID.
    """
    return event_services.approve_event_service(event_id)

@router.post("/events/{event_id}/reject", response_model=EventOut)
async def reject_event(event_id: int, user=Depends(get_current_user)):
    """
    Reject an event by its ID.
    """
    return event_services.reject_event_service(event_id)

@router.delete("/events/{event_id}", response_model=EventOut)
async def delete_event(event_id: int, user=Depends(get_current_user)):
    """
    Delete an event by its ID.
    """
    return event_services.delete_event_service(event_id)

@router.put("/events/{event_id}/status/{status}", response_model=EventOut)
async def update_event_status(event_id: int, status: str, user=Depends(get_current_user)):
    """
    Update the status of an event by its ID.
    """
    return event_services.update_event_status_service(event_id, status)

@router.get("/events/status/{status}", response_model=list[EventOut])
async def get_events_by_status(status: str, user=Depends(get_current_user)):
    """
    Get events by their status.
    """
    return event_services.get_events_by_status_service(status)