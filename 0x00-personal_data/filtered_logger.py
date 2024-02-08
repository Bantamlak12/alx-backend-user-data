#!/usr/bin/env python3
"""
Managing user data
"""
from typing import List
import logging
import re


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
