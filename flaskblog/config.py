class Config:
    SECRET_KEY = '6348bc5ac63090a28b93b21561a53579'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'senderBotAccount@gmail.com'
    MAIL_PASSWORD = 'password'
