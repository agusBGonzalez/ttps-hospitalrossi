from os import environ

class BaseConfig(object):
    """Base configuration."""

    DEBUG = None
    DB_HOST = "bd_name"
    DB_USER = "db_user"
    DB_PASS = "db_pass"
    DB_NAME = "db_name"
    SECRET_KEY = "secret"

    @staticmethod
    def configure(app):
        # Implement this method to do further configuration on your app.
        pass


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    ENV = "development"
    DEBUG = environ.get("DEBUG", True)

    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_USER = environ.get("DB_USER", "MY_DB_USER")
    DB_PASS = environ.get("DB_PASS", "MY_DB_PASS")
    DB_NAME = environ.get("DB_NAME", "MY_DB_NAME")
    DB_ALCH = "mysql+pymysql://%s:%s@%s/%s" % (DB_USER, DB_PASS, DB_HOST, DB_NAME)

class TestingConfig(BaseConfig):
    """Testing configuration."""

    ENV = "testing"
    TESTING = True
    DEBUG = environ.get("DEBUG", True)
    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_USER = environ.get("DB_USER", "MY_DB_USER")
    DB_PASS = environ.get("DB_PASS", "MY_DB_PASS")
    DB_NAME = environ.get("DB_NAME", "MY_DB_NAME")
    DB_ALCH = "mysql+pymysql://usuario:password@localhost/schema"

class ProductionConfig(BaseConfig):
    """Production configuration."""

    ENV = "production"
    DEBUG = environ.get("DEBUG", False)
    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_USER = environ.get("DB_USER", "grupo47")
    DB_PASS = environ.get("DB_PASS", "ZThmYzBkYzFhYTA0")
    DB_NAME = environ.get("DB_NAME", "grupo47")
    DB_ALCH = "mysql+pymysql://grupo47:ZThmYzBkYzFhYTA0@localhost/grupo47"

config = dict(
    development=DevelopmentConfig, testing=TestingConfig, production=ProductionConfig
)
