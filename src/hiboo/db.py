from sqlmodel import create_engine

from hiboo.config import settings

engine = create_engine(settings.database_url, echo=settings.postgres_echo)
