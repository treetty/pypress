#!/usr/bin/env python
#coding=utf-8

"""
    validators.py
    ~~~~~~~~~~~~~

    :license: BSD, see LICENSE for more details.
"""
from wtforms.validators import regexp

from flask_babel import lazy_gettext as _

USERNAME_RE = r'^[\w.+-]+$'

is_username = regexp(USERNAME_RE, 
                     message=_("You can only use letters, numbers or dashes"))

