# logger/logger.py

import logging
import colorlog
from bot.config.bot_config import Config

config = Config()

# def Logger():
#     logger = logging.getLogger('application')

#     # Удаляем все обработчики, чтобы избежать дублирования
#     if logger.hasHandlers():
#         logger.handlers.clear()

#     # Создаем цветной форматтер
#     formatter = colorlog.ColoredFormatter(
#         '%(log_color)s%(asctime)s | %(levelname)s | %(message)s',
#         log_colors={
#             'DEBUG': 'cyan',
#             'INFO': 'green',
#             'WARNING': 'yellow',
#             'ERROR': 'red',
#             'CRITICAL': 'magenta',
#         },
#     )

#     # Создаем консольный обработчик
#     console_handler = logging.StreamHandler()
#     console_handler.setLevel(logging.DEBUG)
#     console_handler.setFormatter(formatter)

#     # Создаем файловый обработчик
#     file_handler = logging.FileHandler(config.logger.PATH, encoding='utf-8')
#     file_handler.setLevel(logging.DEBUG)
#     file_handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(message)s'))

#     # Добавляем обработчики к логгеру
#     logger.addHandler(console_handler)
#     logger.addHandler(file_handler)

#     return logger
