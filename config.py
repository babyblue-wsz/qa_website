JSON_AS_ASCII = False
SECRET_KEY = '23456'

# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'qa'
USERNAME = 'root'
PASSWORD = 'wsz1998'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

# 邮箱设置
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = "654055079@qq.com"
MAIL_PASSWORD = "bnyurmjscywnbdbi"
MAIL_DEFAULT_SENDER = "654055079@qq.com"