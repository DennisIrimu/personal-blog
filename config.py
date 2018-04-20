class Config:
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresq1+psycopg2://dnyt:dimm8450@localhost/dnyt'

config_options ={"production":ProdConfig,"default":DevConfig}
