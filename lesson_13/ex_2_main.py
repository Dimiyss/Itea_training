from ex_2_base_class import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from ex_2_users import User
from ex_2_address import Address


engine = create_engine('postgresql://postgres:123@localhost:5432/postgres')
session = Session(bind=engine)
Base.metadata.create_all(engine)


# print(dir(User))
# print(dir(Address))


# session.add_all([
#     Address(1, 'anna@gmail.com'),
#     Address(2, 'ivan@gmail.com'),
#     Address(3, 'petr@gmail.com'),
#     Address(5, 'jack@gmail.com'),
# ])
# session.commit()

# for address in session.query(Address):
#     print(address)

for user in session.query(User):
    print(user, user.addresses[0].email)