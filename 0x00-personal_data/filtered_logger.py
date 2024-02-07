#!/usr/bin/env python3
"""
Managing user data
"""
from typing import List
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
