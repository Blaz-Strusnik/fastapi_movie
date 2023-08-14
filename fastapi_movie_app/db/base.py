from sqlalchemy.orm import DeclarativeBase

from fastapi_movie_app.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta
