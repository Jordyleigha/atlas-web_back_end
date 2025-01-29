#!/usr/bin/env python3
"""function called filter_datum that returns the log message obfuscated"""
import logging
import re
from typing import List, Tuple


PII_FIELDS: Tuple
[str, str, str, str, str] = ("email", "ssn", "password", "name", "address")


def get_logger() -> logging.Logger:
    """Create and return a logger configured for user data."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()

    formatter = RedactingFormatter(fields=PII_FIELDS)

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


def filter_datum(fields:
                 List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Obfuscate specified fields in a log message."""
    pattern = r'({}){}=([^{}]*)'.format
    ('|'.join(map(re.escape, fields)), re.escape(separator),
     re.escape(separator))
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize the formatter with fields to redact."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record, redacting specified fields."""
        record.msg = filter_datum
        (self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)
