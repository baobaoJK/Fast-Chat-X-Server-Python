from flask import request
from flask_socketio import leave_room

from entitys.result import Result
from entitys.sql.user import User
from services import get_room_list
from utils import socketio, app, get_sql_session

import services


@app.route('/')
def hello_world():  # put application's code here
    return '404'


@app.before_request
def handle_before_request():
    if request.path == '/api/user/login' or request.path == '/api/user/register' or request.path == '/api/user/forget':
        return None

    header = request.headers
    # print(header)
    # 获取token
    token = header.get('Authorization')
    result = Result()

    if token is None:
        result.set_code(-1)
        result.set_message('请先登录')
        result.set_status(401)
        return result.to_dict()


# 连接触发
@socketio.on('connect')
def handle_connect():
    current_connections = len(socketio.server.manager.rooms['/'])
    print(f"Socket 连接数量: {current_connections}")


# 断开连接
@socketio.on('disconnect')
def handle_disconnect():
    current_connections = len(socketio.server.manager.rooms['/'])
    print(f"有人退出了 当前 Socket 连接数量: {current_connections}")

    room_list = get_room_list()

    # 检测 user_name 是不是在 room_list 里
    for item in room_list:
        if item['sid'] == request.sid:
            room_list.remove(item)
            sql_session = get_sql_session()
            user = sql_session.query(User).filter(User.user_name == item['name']).first()
            leave_room(user)

    socketio.send({'type': 'userList', 'data': get_room_list()})


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
