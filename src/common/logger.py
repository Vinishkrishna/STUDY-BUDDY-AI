import logging
import os
from datetime import datetime

LOGS_DIR = "logs"
os.makedirs(LOGS_DIR,exist_ok=True)

LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(
    filename=LOG_FILE,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def get_logger(name):
    logger = logging.getLogger(name) #Creates or retrieves a logger object with the specified name
    logger.setLevel(logging.INFO)
    return logger

'''
The name parameter is a string that identifies your logger.
It is used to label the logger so you can have separate loggers for different parts (modules, classes, components) of your application.

For example, you might have loggers called "database", "api", "auth", etc.
'''
#By setting the level to INFO, the logger will only record log messages that are INFO or higher (INFO, WARNING, ERROR, CRITICAL).
#Messages with a lower level (like DEBUG) will be ignored by this logger.
