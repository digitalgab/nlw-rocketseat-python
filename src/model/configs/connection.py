from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnection:
    def __init__(self):
        self._connection_string = connection_string
        self._engine = self._create_database_engine()
        self.session = None

    def _create_database_engine(self) -> object:
        engine = create_engine(self._connection_string)
        return engine

    def __enter__(self):
        sessionmaker(bind=self._engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
