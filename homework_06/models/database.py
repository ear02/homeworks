from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

__all__ = (
    "db",
)