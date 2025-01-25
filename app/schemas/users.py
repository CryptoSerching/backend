from sqlalchemy import relationship, ForeignKey, Integer, Column, String



class Address():
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String, nullable=True)
    zipcode = Column(String, nullable=True)
    city = Column(String, nullable=True)
    street = Column(String, nullable=True)
    number = Column(String, nullable=True)
    user = relationship("Users", back_populates="address")

class Users():
    __tablename__ = 'users'
    username = Column(String, primary_key=True, unique=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False, type_="password")
    address_id = Column(Integer, ForeignKey('addresses.id'), nullable=True)
    address = relationship("Address", back_populates="user")
    role = relationship("Role", back_populates="users")
    phone = Column(String, nullable=True)
    address = Address()


class Role():
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)


