from sqlalchemy.orm import Session

from twitter_api import models, schemas

####### Users section #######


def read_user(db: Session, user_id: int):
    """Function should query the db for the user matching user_id"""
    return db.query(models.User).filter(models.User.id == user_id).first()


def read_users(db: Session, skip: int = 0, limit: int = 100):
    """Function should return all users with a skip and limit param"""
    return db.query(models.User).offset(skip).limit(limit).all()


def read_user_by_email(db: Session, email: str):
    """Function should query the db for the user with a matching email"""
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    """Function should create a new user in the database"""
    print("CREATE USER...")
    new_user = models.User(email = user.email , 
                           hashed_password = user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



####### Tweets section #######


def read_tweets(db: Session, skip: int = 0, limit: int = 100):
    """Function should return all tweets with a skip and limit param"""
    return db.query(models.Tweet).offset(skip).limit(limit).all()


def create_tweet(db: Session, tweet: schemas.TweetBase, user_id: int):
    print("CREATE tweets...")
    new_tweet = models.Tweet(text= tweet.text , owner_id = user_id)
    db.add(new_tweet)
    db.commit()
    db.refresh(new_tweet)
    return new_tweet


def read_users_tweets(db: Session, user_id: int):
    """Function should return all the tweets for a given user_id"""
    return read_user(db=db, user_id=user_id).tweets
    # 💡 Hint: make use of SQL Alchemy's user.tweets sugar syntax!
    

####### Likes section #######


def create_like(db: Session, like: schemas.LikeCreate, user_id: int):
    """Function should create a new like in the database"""
    pass  # YOUR CODE HERE


def read_like(db: Session, owner_id: int, tweet_id: int):
    """Should check if a user has already liked a tweet"""
    pass  # YOUR CODE HERE


def update_tweet_like_count(db: Session, tweet_id: int, up: bool = True):
    """Edit the number of likes for a given tweet id based on up bool"""
    pass  # YOUR CODE HERE


def read_user_likes(db: Session, user_id: int):
    """Get the likes from a given user"""
    pass  # YOUR CODE HERE


def read_user_liked_tweets(db: Session, user_id: int):
    """Read all liked_tweets from a user"""
    pass  # YOUR CODE HERE
