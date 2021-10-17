#docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:secret@172.17.0.2"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()