from sqlalchemy import create_engine, URL, text
from sqlalchemy.orm import sessionmaker

url = URL.create(
    drivername="postgresql+psycopg2",  # driver name = postgresql + the library we are using (psycopg2)
    username='testuser',
    password='testpassword',
    host='localhost',
    database='testuser',
    port=5432
)

engine = create_engine(url, echo=True)

session_pool = sessionmaker(engine)
