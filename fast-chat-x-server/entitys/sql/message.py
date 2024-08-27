from sqlalchemy import Column, Integer, String, Double, SmallInteger, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.mysql import LONGTEXT

Base = declarative_base()


class Message(Base):
    __tablename__ = 'msg_list'

    msg_id = Column(Integer, primary_key=True, autoincrement=True)
    from_user = Column(String)
    to_user = Column(String)
    msg_content = Column(LONGTEXT)
    msg_date = Column(DateTime)

    def to_dict(self):
        return {
            'msgId': self.msg_id,
            'fromUser': self.from_user,
            'toUser': self.to_user,
            'msgContent': self.msg_content,
            'msgDate': self.msg_date
        }
