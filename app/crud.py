from sqlalchemy.orm import Session
from app.models import URL
from app.schemas import URLCreate
import shortuuid

def create_short_url(db: Session, url_data: URLCreate):

    if url_data.custom_code:
        short_code = url_data.custom_code
    else:
        short_code = shortuuid.ShortUUID().random(length=7)

    existing = db.query(URL).filter(URL.short_code == short_code).first()

    if existing:
        raise ValueError("Short code already exists")

    db_url = URL(
        original_url=url_data.original_url,
        short_code=short_code
    )

    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    return db_url


def get_url_by_code(db: Session, short_code: str):

    return db.query(URL).filter(
        URL.short_code == short_code
    ).first()


def increment_clicks(db: Session, url: URL):

    url.clicks += 1

    db.commit()
    db.refresh(url)

    return url