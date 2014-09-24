from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
date = Table('date', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('date', String(length=64)),
    Column('user_id', Integer),
)

location = Table('location', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('location', String(length=120)),
    Column('date_id', String(length=64)),
)

time = Table('time', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('time', String(length=64)),
    Column('location_id', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['date'].create()
    post_meta.tables['location'].create()
    post_meta.tables['time'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['date'].drop()
    post_meta.tables['location'].drop()
    post_meta.tables['time'].drop()
