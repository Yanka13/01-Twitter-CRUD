from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class User(Base):
    """Class to represent the users table"""

    # Table name
    __tablename__ = "users" 

    # Columns
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    tweets = relationship("Tweet", back_populates="owner") # allows query "user.tweet
    
class Tweet(Base):  # YOUR CODE HERE: Please add "Base" inheritence to this class when you start working on this class, to allow `alembic revision --autogenerate` to take into account this model
    """Class to represent the tweets table"""

    # Table name
    __tablename__ = "tweets" 

    # Columns
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    text = Column(String, nullable=False)
    owner = relationship("User", back_populates="tweets") # allows query "tweet.owner"



class Like():  # YOUR CODE HERE: Please add "Base" inheritence to this class when you start working on Like to allow running `alembic revision --autogenerate` to take into account this model
    """Class to represent the likes table"""

    # Table name
    pass  # YOUR CODE HERE

    # Columns
    pass  # YOUR CODE HERE

    # Relationships
    pass  # YOUR CODE HERE
