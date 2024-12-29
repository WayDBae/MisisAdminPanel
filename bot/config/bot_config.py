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


class Bot:
    def __init__(self):
        self.TOKEN = env("BOT_TOKEN")
        self.THREADED = env.bool("BOT_THREADED", default=False)
        # Инициализация бота
        self.bot = self.init_bot()

    def init_bot(self):
        """Инициализация подключения к боту."""
        return TeleBot(token=self.TOKEN, threaded=self.THREADED)

    def __str__(self):
        return f"Bot(token={self.TOKEN}, threaded={self.THREADED})"


class Weather:
    def __init__(self):
        self.URL = env("WEATHER_URL")
        self.LANG = env("WEATHER_LANG", default="en")
        self.CITY = env("WEATHER_CITY")
        self.UNITS = env("WEATHER_UNITS", default="metric")
        self.APPID = env("WEATHER_APPID")
        self.weather = self.init_weather()

    def init_weather(self):
        """Формируем URL с подстановкой параметров"""
        full_url = self.URL.format(self.CITY, self.UNITS, self.LANG, self.APPID)
        return full_url

    def __str__(self):
        return f"Weather(url={self.URL}, city={self.CITY}, units={self.UNITS}, appid={self.APPID})"


class Config:
    def __init__(self):
        # Инициализация отдельных конфигураций
        self.webhook = Webhook()
        self.database = PostgreSQL()
        self.logger = Logger()
        self.bot = Bot()
        self.DEVELOPER_CHAT_ID = env("DEVELOPER_CHAT_ID")
        self.DEVELOPER_USERNAME = env("DEVELOPER_USERNAME")
        self.weather = Weather()

    def __str__(self):
        return f"Config(bot={self.bot}, logger={self.logger}, webhook={self.webhook}, database={self.database})"
