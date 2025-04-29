from backend.db.base import Base
from backend.db.session import engine

Base.metadata.create_all(bind=engine)