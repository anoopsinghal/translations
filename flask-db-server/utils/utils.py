from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from sqlalchemy.dialects import mysql
from sqlalchemy.sql import text

Session = None
Engine = None

def create_db_engine(db_conn_string):
    global Engine
    #max_overflow is unlimited.
    if not Engine:
        Engine = create_engine(db_conn_string,
                         pool_size=10,
                         max_overflow=-1,
                         pool_recycle=3600,
                         pool_pre_ping=True,
                         pool_use_lifo=True)
    # end if

    return Engine
#end create_db_engine

def create_db_session(engine):
    global Session
    if not Session:
        Session = sessionmaker(bind=engine)
        # todo: setup connection pooling properties
    return Session()
# end create_db_session