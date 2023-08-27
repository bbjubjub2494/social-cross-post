import json
import os
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

with open("/run/agenix/social-cross-post/config.json") as f:
    vars().update(json.load(f))

class Config(object):
    SECRET_KEY = os.urandom(24)
    SESSION_TYPE = 'filesystem'
    SESSION_FILE_DIR = "/var/lib/social-cross-post"
    VERSION = "1.0."
    SQLALCHEMY_DATABASE_URI = 'sqlite:////var/lib/social-cross-post/posts.db'
    SCHEDULER_JOBSTORES = {
        'default': SQLAlchemyJobStore(url='sqlite:////var/lib/social-cross-post/jobs.db')
    }
    SCHEDULER_API_ENABLED = True
