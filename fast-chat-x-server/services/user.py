import hashlib
from datetime import datetime

from flask import request
from flask_socketio import emit
from sqlalchemy import asc

from entitys.result import Result
from entitys.sql.message import Message
from entitys.sql.user import User
from services.room import get_room_list
from utils import app, get_sql_session, socketio
from utils.user import check_user


# 用户登录
@app.route('/api/user/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    result = Result()

    if username is None or password is None:
        result.set_status(200)
        result.set_code(-1)
        result.set_message("用户名或密码不能为空")
        return result.to_dict()

    sql_session = get_sql_session()
    user = sql_session.query(User).filter_by(user_account=username, user_password=password).first()

    if user is None:
        result.set_status(200)
        result.set_code(-1)
        result.set_message("登录失败，请检查用户名和密码")
        return result.to_dict()

    result.set_status(200)
    result.set_code(1)
    result.set_message("登陆成功")
    result.set_data(user.to_dict())

    return result.to_dict()


@socketio.on('login')
def handle_login(data):
    token = data['token']

    sql_session = get_sql_session()

    user = sql_session.query(User).filter_by(user_token=token).first()
    # print(user.to_dict())
    # 获取房间列表
    room_list = get_room_list()
    # 检测 user_name 是不是在 room_list 里
    for item in room_list:
        if item['name'] == user.user_name:
            sid = item['sid']
            print(sid)
            emit('message', {'type': 'kick', 'message': '你的账号在别处登录'}, room=sid)
            break


# 用户注册
@app.route('/api/user/register', methods=['POST'])
def handle_register():
    username = request.json.get('username')
    password = request.json.get('password')
    phone = request.json.get('phone')

    result = Result()

    if username is None or password is None or phone is None:
        result.set_status(200)
        result.set_code(-1)
        result.set_message("参数错误")
        return result.to_dict()

    sql_session = get_sql_session()
    user_by_account = sql_session.query(User).filter_by(user_account=username).first()

    if user_by_account is not None:
        result.set_status(200)
        result.set_code(-1)
        result.set_message("用户名已存在")
        return result.to_dict()

    user_by_phone = sql_session.query(User).filter_by(user_phone=phone).first()
    if user_by_phone is not None:
        result.set_status(200)
        result.set_code(-1)
        result.set_message("手机号已存在")
        return result.to_dict()

    new_user = User()
    new_user.user_token = hashlib.md5(str(username).encode(encoding='UTF-8')).hexdigest()
    new_user.user_account = username
    new_user.user_password = password
    new_user.user_phone = phone
    new_user.user_name = username
    new_user.user_img = 'user00.jpg'
    new_user.user_status = 1
    new_user.create_time = datetime.now()

    sql_session.add(new_user)
    sql_session.commit()

    result.set_status(200)
    result.set_code(1)
    result.set_message("注册成功")
    return result.to_dict()


# 忘记密码
@app.route('/api/user/forget', methods=['POST'])
def handel_forget_password():
    result = Result()
    username = request.json.get('username')
    password = request.json.get('password')
    phone = request.json.get('phone')

    sql_session = get_sql_session()
    user_by_account = sql_session.query(User).filter_by(user_account=username).first()
    if user_by_account is None:
        result.set_status(200)
        result.set_code(-1)
        result.set_message("用户不存在")
        return result.to_dict()

    user_by_phone = sql_session.query(User).filter_by(user_phone=phone).first()
    if user_by_phone is None or user_by_account.user_phone != user_by_phone.user_phone:
        result.set_status(200)
        result.set_code(-1)
        result.set_message("手机号不正确")
        return result.to_dict()

    user_by_phone.user_password = password
    sql_session.commit()

    result.set_status(200)
    result.set_code(1)
    result.set_message("修改密码成功")
    return result.to_dict()


# 获取用户信息
@app.route('/api/user', methods=['GET'])
def handel_get_user():
    check_user()

    # 获取token
    token = request.headers.get('Authorization').split(' ')[1]
    result = Result()

    sql_session = get_sql_session()
    user = sql_session.query(User).filter_by(user_token=token).first()

    result.set_code(1)
    result.set_message('获取用户信息成功')
    result.set_status(200)
    result.set_data(user.to_dict())

    return result.to_dict()


# 获取消息列表
@app.route('/api/user/message', methods=['GET'])
def handel_get_message():
    check_user()

    page = request.args.get('page', 1, type=int)

    sql_session = get_sql_session()

    # 创建子查询
    subquery = sql_session.query(
        Message.msg_id,
        User.user_name.label('name'),
        Message.msg_content.label('message'),
        Message.msg_date.label('time'),
        User.user_img.label('img')).join(Message,
                                         User.user_account == Message.from_user).order_by(
        Message.msg_id.desc()).limit(20).offset((page - 1) * 20).subquery()

    # 在外部查询中按 id 正序排列
    query = sql_session.query(subquery).order_by(asc(subquery.c.msg_id))

    # 执行查询
    results = query.all()

    message_list = []
    for msg_id, name, message, time, img in results:
        message_list.append({
            'id': msg_id,
            'name': name,
            'message': message,
            'time': time,
            'img': img
        })

    result = Result()
    result.set_code(1)
    result.set_message('获取消息列表成功')
    result.set_status(200)
    result.set_data(message_list)

    return result.to_dict()


# 发送消息
@socketio.on('sendMessage')
def handle_send_message(data):
    # 存储信息
    sql_session = get_sql_session()
    sql_session.add(Message(
        msg_content=data['message'],
        from_user=data['from'],
        msg_date=datetime.now()
    ))
    sql_session.commit()

    # 广播消息
    data['time'] = datetime.now().__str__()
    socketio.send({'type': 'message', 'data': data})


# 修改信息
@app.route('/api/user/updateInfo', methods=['POST'])
def update_info():
    check_user()

    # 获取token
    token = request.headers.get('Authorization').split(' ')[1]
    result = Result()
    sql_session = get_sql_session()
    user = sql_session.query(User).filter_by(user_token=token).first()

    user.user_name = request.json.get('userInfoForm')['username']
    sql_session.commit()

    result.set_status(200)
    result.set_code(1)
    result.set_message("修改信息成功")
    return result.to_dict()
