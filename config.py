import os

# Версия
NLAB_SOVA_VERSION = os.getenv('NLAB_SOVA_VERSION')

# Подключение к Sentry
NLAB_SOVA_SENTRY_DSN = os.getenv('NLAB_SOVA_SENTRY_DSN')

# Подключение отладки
NLAB_SOVA_DEBUG = os.getenv('NLAB_SOVA_DEBUG', False)

# Адрес диалогового процессора
NLAB_SOVA_ENGINE_HOST = os.getenv('NLAB_SOVA_ENGINE_HOST', 'tcp:engine:2255')

# DSN соединения с базой данных
NLAB_SOVA_DB_DSN = os.getenv('NLAB_SOVA_DB_DSN', 'sqlite://var/db/db.sqlite3')

# Подключенные расширения
NLAB_EXTENSION_PRIORITY = {
    "context": {
        "context": 0
    },
    "context.store": {
        "context": 0
    },
    "preprocessor": {
        "preprocessor": 0,
    },
    "postprocessor": {
        "postprocessor": 0
    },
    "journal": {
        "journal": 0
    }
}
