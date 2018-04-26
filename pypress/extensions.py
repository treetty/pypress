#!/usr/bin/env python
#coding=utf-8

from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_cache import Cache
from flask_uploads import UploadSet, IMAGES

__all__ = ['mail', 'db', 'cache', 'photos']

mail = Mail()
db = SQLAlchemy()
cache = Cache()
photos = UploadSet('photos', IMAGES)

