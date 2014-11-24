Title: DJANGO: new LOGGING settings
Date: 2012-04-26 04:00
Modified: 
Category: Programming
Tags: Django
Slug: new_logging_settings
Lang: en
Authors: znotdead
Summary: Here is example of LOGGING which creates LOG_DIR and logs in debug.log and error.log and mail to admins exceptions as before django1.3

### new LOGGING settings

```python
LOG_LEVEL = DEBUG and 'DEBUG' or 'INFO'
FORMAT = '[%(asctime)s] [%(levelname)s] [PID: '+str(os.getpid())+'] [%(name)s]:  %(message)s'

LOG_FILE = os.path.join(LOG_DIR, 'debug.log')
ERR_FILE = os.path.join(LOG_DIR, 'error.log')

if not os.path.exists(LOG_DIR):
    try:
        os.mkdir(LOG_DIR)
    except:
        raise Exception("CAN NOT CREATE LOG DIR: %s" % LOG_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': FORMAT
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'log': {
            'level': LOG_LEVEL,
            'formatter': 'verbose',
            'class': 'log_handlers.TimedRotatingFileHandlerSafe',
            'filename': LOG_FILE,
            'when': LOG_INTERVAL,
        },
        'error': {
            'level': 'ERROR',
            'formatter': 'verbose',
            'class': 'log_handlers.TimedRotatingFileHandlerSafe',
            'filename': ERR_FILE,
            'when': LOG_INTERVAL,
        }
    },
    'loggers': {
        'django': {
            'handlers':['null'],
            'propagate': False,
            'level':'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins', 'log', 'error'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
    'root': {
        'handlers': ['log', 'error',],
        'level': LOG_LEVEL,
    },
}
```
