# config/custom_config.py
import environ
from peewee import PostgresqlDatabase
from telebot import TeleBot

env = environ.Env()
environ.Env.read_env(".env")


class Webhook:
    def __init__(self):
        self.HOST = env("WEBHOOK_HOST")
        self.PORT = env.int("WEBHOOK_PORT", 443)
        self.LISTEN = env("WEBHOOK_LISTEN", default="0.0.0.0")
        self.MODE = env("MODE", default="dev")

    def __str__(self):
        return f"Webhook(host={self.HOST}, port={self.PORT}, listen={self.LISTEN}, mode={self.MODE})"


class PostgreSQL:
    def __init__(self):
        self.NAME = env("DB_NAME")
        self.USER = env("DB_USER", default="postgres")
        self.PASSWORD = env("DB_PASSWORD", default="postgres")
        self.HOST = env("DB_HOST", default="localhost")
        self.PORT = env.int("DB_PORT", default=5432)

        # Инициализация базы данных
        self.db = self.init_db()

    def init_db(self):
        """Инициализация подключения к базе данных."""
        return PostgresqlDatabase(
            self.NAME,
            user=self.USER,
            password=self.PASSWORD,
            host=self.HOST,
            port=self.PORT,
        )

    def __str__(self):
        return f"PostgreSQL(db={self.NAME}, user={self.USER}, host={self.HOST}, port={self.PORT})"


class Logger:
    def __init__(self):
        self.PATH = env("LOGGER_PATH", default="logs/")
        self.TYPE = env("LOGGER_TYPE", default="file")
        self.LEVEL = env("LOGGER_LEVEL", default="INFO")

    def __str__(self):
        return f"Logger(path={self.PATH}, type={self.TYPE})"


class Config:
    def __init__(self):
        # Инициализация отдельных конфигураций
        self.webhook = Webhook()
        self.database = PostgreSQL()
        self.logger = Logger()

    def __str__(self):
        return f"Config(logger={self.logger}, webhook={self.webhook}, database={self.database})"
