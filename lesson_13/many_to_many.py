from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, create_engine, ForeignKey
from sqlalchemy.orm import Session, relationship

Base = declarative_base()

engine = create_engine('postgresql://postgres:123@localhost:5432/postgres')


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)

    projects = relationship('Project', secondary='users_project', back_populates='users')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'User: {self.name}'


class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)

    users = relationship('User', secondary='users_project', back_populates='projects')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Project: {self.name}'


class UserProject(Base):
    __tablename__ = 'users_project'

    id = Column(Integer, primary_key=True)
    about = Column(Text, nullable=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    project_id = Column(Integer, ForeignKey('projects.id'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Project: {self.name}'


Base.metadata.create_all(engine)

# with Session(bind=engine) as session:
#     user_anna = User('Anna')
#     user_ivan = User('Ivan')
#     user_petr = User('Petr')
#
#     prj_1 = Project('Project #1')
#     prj_2 = Project('Project #2')
#
#     session.add_all([user_anna, user_ivan, user_petr,
#                      prj_1, prj_2])
#     session.commit()
#
#     prj_1.users = [user_anna, user_ivan]
#     prj_2.users = [user_petr]
#
#     session.commit()

with Session(bind=engine) as session:
    print(session.query(User).filter(User.id == 1).one().projects)

    print(session.query(Project).filter(Project.id == 1).one().users)