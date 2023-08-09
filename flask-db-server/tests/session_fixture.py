from sqlalchemy import create_engine
from utils.utils import create_db_session
import pytest

from orm.article import Article
from orm.article import Base

@pytest.fixture(scope="session")
def session():
  print ("setting up session")
  engine = create_engine("sqlite+pysqlite:///:memory:")
  db_session = create_db_session(engine)

  Base.metadata.create_all(engine)

  yield db_session
  db_session.close()
# end session



