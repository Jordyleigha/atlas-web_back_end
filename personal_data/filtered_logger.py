#!/usr/bin/env python3
"""function called filter_datum that returns the log message obfuscated"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Obfuscate specified fields in a log message.

    Args:
        fields (List[str]): A list of field names (strings) that should be
            obfuscated in the log message.
        redaction (str): The string that will replace the specified fields
            in the log message.
        message (str): The log line that contains the fields to be obfuscated.
        separator (str): The character that separates the fields in the log
            line (message).

    Returns:
        str: The log message with the specified fields obfuscated by the
            redaction string.
    """
    # Create a regex pattern that matches the fields to be obfuscated
    pattern = r'({}){}=([^{}]*)'.format('|'.join(map(re.escape, fields)), re.escape(separator), re.escape(separator))

    return re.sub(pattern, lambda m: f"{m.group(0).split('=')[0]}={redaction}", message)
