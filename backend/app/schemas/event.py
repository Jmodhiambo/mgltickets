#!/usr/bin/env python3
"""Event schemas for MGLTickets."""

from datetime import datetime
from app.schemas.base import BaseModelEAT
from typing import Optional

from app.schemas.user import UserOut
from app.schemas.booking import BookingOut
from app.schemas.ticket_type import TicketTypeOut

class EventOut(BaseModelEAT):
    """Base schema for Event."""
    id: int
    title: str
    organizer_id: int
    description: Optional[str] = None
    venue: str
    start_time: datetime
    end_time: datetime
    flyer_url: str
    status: str
    created_at: datetime
    updated_at: datetime
    organizer: UserOut
    bookings: list[BookingOut] = []
    ticket_types: list[TicketTypeOut] = []

    class Config:
        from_attributes = True

class EventCreate(BaseModelEAT):
    """Schema for creating a new Event."""
    title: str
    organizer_id: int
    description: Optional[str] = None
    venue: str
    start_time: datetime
    end_time: datetime
    flyer_url: str

    class Config:
        from_attributes = True

class EventUpdate(BaseModelEAT):
    """Schema for updating an existing Event."""
    title: Optional[str] = None
    description: Optional[str] = None
    venue: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    flyer_url: Optional[str] = None
    status: Optional[str] = None

    class Config:
        from_attributes = True