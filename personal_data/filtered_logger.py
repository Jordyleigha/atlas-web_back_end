#!/usr/bin/env python3
"""function called filter_datum that returns the log message obfuscated"""
import re


def filter_datum(fields, redaction, message, separator):
    """Obfuscate specified fields in a log message.

    Args:
        fields (list of str): A list of field names (strings) that should be
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
    return re.sub(r'(?<=' + re.escape(separator) + r'|^)(?:' + '|'.join(map(re.escape, fields)) + r')(?=' + re.escape(separator) + r'|$)', redaction, message)