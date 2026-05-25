from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import URLCreate
from app import crud
import os

router = APIRouter()

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")

@router.post("/shorten")
def shorten_url(url_data: URLCreate, db: Session = Depends(get_db)):
    try:
        url = crud.create_short_url(db, url_data)

        return {
            "id": url.id,
            "original_url": url.original_url,
            "short_code": url.short_code,
            "short_url": f"{BASE_URL}/{url.short_code}",
            "clicks": url.clicks,
            "created_at": url.created_at
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{short_code}")
def redirect_to_original(short_code: str, db: Session = Depends(get_db)):

    url = crud.get_url_by_code(db, short_code)

    if not url:
        raise HTTPException(status_code=404, detail="Short URL not found")

    crud.increment_clicks(db, url)

    return RedirectResponse(url=url.original_url)