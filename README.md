# Fast-Chat-X-Server-Python
![FCX](images/FCX.png)

名称：Fast-Chat-X / 极聊X

作者：KSaMar

日期：2024/08/25 - 2024/08/27

描述：一个在线的即时聊天网页聊天室

点我去客户端：[客户端](https://github.com/baobaoJK/Fast-Chat-X-Client-Python)

## 开发环境

开发软件：PyCharm 2023.2.3

Python 版本：Python 3.7



### 技术栈

项目采用以下技术：

Python3 + Flask + SocketIO + SQLAlchemy + MySQL

![极聊X 技术栈](images/%E6%9E%81%E8%81%8AX%20%E6%8A%80%E6%9C%AF%E6%A0%88.png)

## 项目介绍

采用 Vue3 + SocketIO 的即时在线多人聊天室网页项目（客户端）

功能模块：用户登录、用户注册、用户忘记密码、群聊等（未来会弄更多）

可以发送文本 / 符号表情与 emoji 表情 😊

消息可以存取到数据库中



## 项目图片

前往服务端进行查看

### 目前完成的功能

![极聊X 功能](images/%E6%9E%81%E8%81%8AX%20%E5%8A%9F%E8%83%BD.png)

## 项目部署

使用 pip 安装所需要的包，使用 PyCharm 启动 Fast-Chat-X-Server 服务

### 数据库服务

在 utils 包下的 sql_connect.py 里修改你自己的 MySQL 数据库信息，记得导入数据库数据

```python
SQL_USERNAME = 'root'           # 数据库用户名
SQL_PASSWORD = '123456'         # 数据库密码
SQL_HOST = 'localhost'          # 数据库地址
SQL_PORT = '3306'               # 数据库端口
SQL_DATABASE = 'fast_chat_x'    # 数据库名称
```



## Bilibili

欢迎在哔哩哔哩上关注我

[Bilibili](https://space.bilibili.com/51110915)
