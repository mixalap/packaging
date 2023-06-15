from pydantic import BaseSettings


class Settings(BaseSettings):
    LEVEL: str

    class Config:
        env_prefix = 'LOGGING_'

    @property
    def LOGGING_CONFIG(self):
        fmt = '%(asctime)s.%(msecs)03d [%(levelname)s]|[%(name)s]: %(message)s'
        datetime_fmt = '%Y-%m-%d %H:%M:%S'

        config = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'default': {
                    'format': fmt,
                    'datefmt': datetime_fmt,
                },
            },
            'handlers': {
                'default': {
                    'level': self.LEVEL,
                    'formatter': 'default',
                    'class': 'logging.StreamHandler',
                    'stream': 'ext://sys.stdout',
                },
            },
            'loggers': {
                '': {
                    'handlers': ['default'],
                    'level': self.LEVEL,
                    'propagate': False,
                },
            },
        }

        return config
