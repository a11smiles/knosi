"""
FastAPI dependencies (authentication, etc.)
"""
from typing import Optional
from fastapi import Header, Query, HTTPException
from core.config import API_SECRET_KEY


async def verify_api_key(x_api_key: Optional[str] = Header(None)):
    """Verify API key if authentication is enabled."""
    if API_SECRET_KEY and API_SECRET_KEY != "change-me-in-production":
        if not x_api_key or x_api_key != API_SECRET_KEY:
            raise HTTPException(status_code=401, detail="Invalid or missing API key")


async def verify_api_key_query_or_header(
    x_api_key: Optional[str] = Header(None),
    api_key: Optional[str] = Query(None)
):
    """Verify API key from either header or query parameter (for download links)."""
    if API_SECRET_KEY and API_SECRET_KEY != "change-me-in-production":
        # Check header first, then query parameter
        provided_key = x_api_key or api_key
        if not provided_key or provided_key != API_SECRET_KEY:
            raise HTTPException(status_code=401, detail="Invalid or missing API key")
