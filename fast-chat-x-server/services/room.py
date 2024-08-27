from flask import request
from flask_socketio import join_room

from entitys.sql.user import User
from utils import socketio, get_sql_session

# 用户列表
room_list = []


# 加入聊天室
@socketio.on('joinRoom')
def handle_join_room(data):
    sql_session = get_sql_session()
    user = sql_session.query(User).filter(User.user_token == data['token']).first()

    # user_data = {'user': user.to_dict(), 'sid': request.sid}
    print(f"{user.user_name} 加入了房间")
    join_room(user)

    # 检测 user_name 是不是在 room_list 里
    if not any(item['name'] == user.user_name for item in room_list):
        data = {'sid': request.sid, 'name': user.user_name, 'img': user.user_img, 'token': user.user_token}
        room_list.append(data)
    else:
        for item in room_list:
            if item['name'] == user.user_name:
                item['sid'] = request.sid

    for user in room_list:
        print(user)

    socketio.send({'type': 'userList', 'data': get_room_list()})


# 获取房间列表
def get_room_list():
    return room_list


