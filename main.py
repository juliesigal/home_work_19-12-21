import sys
from datetime import datetime
from Kita import Kita
from sqlalchemy import text
from db_config import local_session, create_all_entities
from Students import Students
from Db_repo import DbRepo

# create tables
create_all_entities()

repo = DbRepo(local_session)
