from sqlalchemy import create_engine, URL

url = URL.create(
    drivername="postgresql+psycopg2",  # driver name = postgresql + the library we are using (psycopg2)
    username='testuser',
    password='testpassword',
    host='localhost',
    database='testuser',
    port=5432
)

engine = create_engine(url, echo=True)

print('engine created successfully')