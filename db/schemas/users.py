from sqlalchemy import ForeignKey, Integer, Column, String, Table
from sqlalchemy.orm import relationship
from db.engine import Base

# 中間テーブルの定義
user_roles = Table(
    'user_roles',
    Base.metadata,
    Column('user_id', String, ForeignKey('users.username')),
    Column('role_id', Integer, ForeignKey('roles.id')),
)

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String, nullable=True)
    zipcode = Column(String, nullable=True)
    city = Column(String, nullable=True)
    street = Column(String, nullable=True)
    number = Column(String, nullable=True)
    user = relationship("Users", back_populates="address")

class Users(Base):
    __tablename__ = 'users'
    username = Column(String, primary_key=True, unique=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    address_id = Column(Integer, ForeignKey('addresses.id'), nullable=True)
    address = relationship("Address", back_populates="user", single_parent=True)
    phone = Column(String, nullable=True)
    roles = relationship("Role", secondary=user_roles, back_populates="users")
        

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    users = relationship("Users", secondary=user_roles, back_populates="roles")


