DEBUG = False
TEMPLATE_DEBUG = False


DEFAULT_FILE_STORAGE = 'gaekit.storages.CloudStorage'
GS_BUCKET_NAME = 'wagtaildemo'


COMPRESS_STORAGE = 'compressor.storage.CompressorFileStorage'
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True


DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'wagtaildemo',
         'USER': 'root',
         'HOST': '/cloudsql/wagtaildemo:dev',
         'PORT': '',
         'PASSWORD': '',
         'CONN_MAX_AGE': 0,  # cloudsql can handle only 12 connections per instance
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

CACHES = {
    'default': {
        'BACKEND': 'gaekit.caches.GAEMemcachedCache',
        'TIMEOUT': 300,
    }
}

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

# If we don't have SERVER_SOFTWARE set, we're running migrations,
# so switch to IP+username/password access
import os
if not os.environ.get('SERVER_SOFTWARE'):
    DATABASES['default']['HOST'] = '190.100.100.100'
    DATABASES['default']['PASSWORD'] = 'some_password_here'


