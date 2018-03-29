class Config(object):
    """
    Common configurations
    """
    # Put any configurations here that are common across all environments
    DEBUG = True


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


class TestConfig(Config):
    """
    Testing configurations
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestConfig
}