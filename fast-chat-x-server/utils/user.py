from flask import request

from entitys.result import Result
from entitys.sql.user import User
from utils import get_sql_session


# 检测用户
def check_user():
    # 获取token
    token = request.headers.get('Authorization').split(' ')[1]
    result = Result()
    sql_session = get_sql_session()
    user = sql_session.query(User).filter_by(user_token=token).first()

    if user is None:
        result.set_code(-1)
        result.set_message('请先登录')
        result.set_status(401)
        return result.to_dict()
