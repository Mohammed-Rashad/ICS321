from functools import wraps
from flask import Flask, request, jsonify
import jwt
def validate_date(date_str):
    from datetime import datetime
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        return None
