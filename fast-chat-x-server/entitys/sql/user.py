from sqlalchemy import Column, Integer, String, Double, SmallInteger, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user_list'

    user_id = Column(Integer, primary_key=True)
    user_token = Column(String)
    user_account = Column(String)
    user_password = Column(String)
    user_phone = Column(String)
    user_name = Column(String)
    user_img = Column(String)
    user_status = Column(SmallInteger)
    create_time = Column(DateTime)

    def to_dict(self):
        return {
            'userId': self.user_id,
            'userToken': self.user_token,
            'userAccount': self.user_account,
            'userPhone': self.user_phone,
            'userName': self.user_name,
            'userImg': self.user_img,
            'createTime': str(self.create_time)
        }
