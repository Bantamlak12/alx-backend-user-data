#!/usr/bin/env python3
"""
Managing user data
"""
from mysql.connector import MySQLConnection
from typing import List
import logging
import re
import os


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    parameters:
    - fields List(str): A list of strings representing all fields to obfuscate
    - redaction (str): A string representing by what the field will be
      obfuscated
    - message (str): A string representing the log line
    - separator (str): A string representing by which character is
      separating all fields in the log line (message)
    Returns:
    - The log obfuscated
    """
    log = message
    for field in fields:
        log = re.sub(f'{field}=.*?{separator}',
                     f'{field}={redaction}{separator}', log)
    return log


def get_db():
    """ Returns a connector to the database
    """
    # Retrieving the values of an enviroment variable with default values
    username = os.environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.environ.get("PERSONAL_DATA_DB_NAME")

    connection = MySQLConnection(user=username, password=password,
                                 host=host, database=db_name)
    return connection


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ';'

    def __init__(self, fields: List[str]):
        """ Initialize
        parameters:
        - fields List[str]: List of strings
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        parameters:
        - Logging recored
        """
        formatted_recored = super().format(record)
        log = filter_datum(self.fields, self.REDACTION, formatted_recored,
                           self.SEPARATOR)
        return log


def get_logger() -> logging.Logger:
    """ A function that returns a logging.Loggeer object
    """
    # Name the logger to "user_data"
    logger = logging.getLogger("user_data")

    # Setting lgging level to logging.INFO
    logger.setLevel(logging.INFO)

    # It should not propagate messages to other loggers
    logger.propagate = False

    # Having StreamHandler with RedactingFormatter as formatter
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(list(PII_FIELDS))
    stream_handler.setFormatter(formatter)
    # Add the StreamHandler to the logger
    logger.addHandler(stream_handler)

    return logger
