from datetime import datetime

from sqlalchemy import MetaData, Integer, String, TIMESTAMP, Table, Column, Boolean

metadata=MetaData()

users=Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String, nullable=False),
    Column('username', String, nullable=False),
    Column('hashed_password', String, nullable=False),
    Column('register_at', TIMESTAMP, default=datetime.utcnow()),
    Column('is_active', Boolean, default=True, nullable=True),
    Column('is_superuser', Boolean, default=True, nullable=True),
    Column('is_verified', Boolean, default=True, nullable=True),

)
