log_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'programa': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s (message)s'
        },
        'trem': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s %(message)s'
        }
    },
    'handlers': {
        'monitor': {
            'class': 'logging.StreamHandler',
            'formatter': 'programa',
            'level': 'INFO'
        },
        'log_erro_programa': {
            'class': 'logging.FileHandler',
            'filename': 'programa_erros.log',
            'mode': 'a',
            'formatter': 'programa',
            'level': 'ERROR'
        },
        'log_debug_programa': {
            'class': 'logging.FileHandler',
            'filename': 'programa_debug',
            'mode': 'w',
            'formatter': 'programa',
            'level': 'DEBUG'
        },
        'log_trem': {
            'class': 'logging.FileHandler',
            'filename': 'trem_eventos.log',
            'mode': 'a',
            'formatter': 'trem',
            'level':'ERROR'
        },
    },
    'loggers': {
        'log_programa': {
            'handlers': ['monitor', 'log_erro_programa', 'log_debug_programa'],
            'level': 'DEBUG',
            'propagate': False
        },
        'log_trem':{
            'handlers': ['log_trem'],
            'level': 'DEBUG',
            'propagate': False
        }
    },
    'root': {
        'handlers': ['monitor'],
        'level': 'DEBUG'
    }
}

from logging.config import dictConfig

dictConfig(log_config)



