from pydantic import BaseModel

# User section


class UserBase(BaseModel):
    email : str 
    


class UserCreate(UserBase):
    password : str  


class User(UserBase):
    id: int
    
    class Config:
        orm_mode = True
        


# Tweet section


class TweetBase(BaseModel):
    text: str


class Tweet(TweetBase):
    id: int
    owner_id: int
    
    class Config:
        orm_mode = True




# Like section


class LikeBase(BaseModel):
    pass  # YOUR CODE HERE


class LikeCreate(LikeBase):
    pass  # YOUR CODE HERE


class Like(LikeBase):
    pass  # YOUR CODE HERE
