from datetime import UTC, datetime

from sqlalchemy import DateTime, Text
from sqlmodel import Field, SQLModel


class JobOffer(SQLModel, table=True):
    __tablename__ = "job_offers"

    id: int | None = Field(default=None, primary_key=True)
    raw_text: str = Field(sa_type=Text)
    title: str | None = Field(default=None, max_length=255)
    company: str | None = Field(default=None, max_length=255)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        sa_type=DateTime(timezone=True),
    )
