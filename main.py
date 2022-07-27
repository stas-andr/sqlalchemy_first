from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/sqlalchemy_tuts')
engine.connect()

print(engine)

