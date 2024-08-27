from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# 获取数据库连接
def get_sql_session():

    # 数据库引擎和会话创建

    SQL_USERNAME = 'root'           # 数据库用户名
    SQL_PASSWORD = '123456'         # 数据库密码
    SQL_HOST = 'localhost'          # 数据库地址
    SQL_PORT = '3306'               # 数据库端口
    SQL_DATABASE = 'fast_chat_x'    # 数据库名称

    engine = create_engine(f'mysql+pymysql://{SQL_USERNAME}:{SQL_PASSWORD}@{SQL_HOST}:{SQL_PORT}/{SQL_DATABASE}')
    Session = sessionmaker(bind=engine)
    sql_session = Session()

    return sql_session
