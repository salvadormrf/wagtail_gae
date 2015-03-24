
DEFAULT_FILE_STORAGE = 'gaekit.storages.CloudStorage'
GS_BUCKET_NAME = 'demo'


COMPRESS_STORAGE = 'compressor.storage.CompressorFileStorage'
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True


# CREATE DATABASE `wagtail_gae_mysql` CHARACTER SET utf8 COLLATE utf8_general_ci;


DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'wagtail_gae_new',
         'USER': 'root',
         'PASSWORD': 'root',
         'HOST': '',  # Set to empty string for localhost.
         'PORT': '',  # Set to empty string for default.
         'CONN_MAX_AGE': 600,  # number of seconds database connections should persist for
        'OPTIONS': {
            'sql_mode': 'TRADITIONAL',
            'charset': 'utf8',
            'init_command': 'SET '
                'storage_engine=INNODB,'
                'character_set_connection=utf8,'
                'collation_connection=utf8_bin,'
                'SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED',
        }  # Now we have a mild degree of confidence :-)
     }
 }

FILE_UPLOAD_HANDLERS = ('django.core.files.uploadhandler.MemoryFileUploadHandler',)
FILE_UPLOAD_MAX_MEMORY_SIZE = 262144000 # the django default: 2.5MB


"""
CACHES = {
    'default': {
        'BACKEND': 'gaekit.caches.GAEMemcachedCache',
        'TIMEOUT': 0,
    }
}
"""

""" for sqlite3
from gaekit.boot import break_sandbox
break_sandbox()
"""

