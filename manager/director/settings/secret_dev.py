# This file is in Git. For local customizations, edit secret.py instead.

from typing import Dict, Optional

DEBUG = True

REDIS_HOST = "127.0.0.1"
REDIS_PORT = "6379"

CHANNELS_REDIS_DB = 0
CHANNELS_REDIS_PREFIX = "manager-channels:"

CELERY_BROKER_URL = "redis://{}:{}/2".format(REDIS_HOST, REDIS_PORT)

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": ["redis://{}:{}/{}".format(REDIS_HOST, REDIS_PORT, CHANNELS_REDIS_DB)],
            "prefix": CHANNELS_REDIS_PREFIX,
        },
    }
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "127.0.0.1",
        "PORT": "5432",
        "NAME": "manager",
        "USER": "manager",
        "PASSWORD": "pwd",
    },
}

DIRECTOR_APPSERVER_HOSTS = ["localhost:5000"]

DIRECTOR_APPSERVER_WS_HOSTS = ["localhost:5010"]

SITE_URL_FORMATS: Dict[Optional[str], str] = {
    None: "http://127.0.0.1:8081/{}/",
}
