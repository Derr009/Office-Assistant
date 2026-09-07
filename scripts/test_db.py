from sqlalchemy import text
from app.database.connection import engine

with engine.connect() as connection:
    result = connection.execute(text("select current_database()"))
    print("Connected to:", result.scalar())
