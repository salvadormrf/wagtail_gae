# -*- coding: utf-8 -*-
from google.appengine.ext import blobstore
from google.appengine.api import images

from django.conf import settings
from django.core.files.storage import Storage

import mimetypes
import cloudstorage
import os
import datetime
import logging
import urlparse


DEFAULT_SIZE = None
if hasattr(settings, 'IMAGESERVICE_DEFAULT_SIZE'):
    DEFAULT_SIZE = getattr(settings, 'IMAGESERVICE_DEFAULT_SIZE')

SECURE = True
if hasattr(settings, 'IMAGESERVICE_SECURE_URLS'):
    SECURE = getattr(settings, 'IMAGESERVICE_SECURE_URLS')

HEADERS = {'x-goog-acl': 'public-read'}
if hasattr(settings, 'IMAGESERVICE_UPLOAD_HEADERS'):
    HEADERS = getattr(settings, 'IMAGESERVICE_UPLOAD_HEADERS')


class CloudStorage(Storage):

    def __init__(self, **kwargs):
        cloudstorage.validate_bucket_name(settings.GS_BUCKET_NAME)
        self.bucket_name = '/' + settings.GS_BUCKET_NAME

    def delete(self, filename):
        assert(filename)
        try:
            cloudstorage.delete(os.path.join(self.bucket_name, filename))
        except cloudstorage.NotFoundError:
            pass

    def exists(self, filename):
        try:
            cloudstorage.stat(os.path.join(self.bucket_name, filename))
            return True
        except cloudstorage.NotFoundError:
            return False

    def _open(self, filename, mode):
        print "#### open", os.path.join(self.bucket_name, filename), self.exists(filename)
        
        readbuffer = cloudstorage.open(os.path.join(self.bucket_name, filename), 'r')
        readbuffer.open = lambda x: True
        return readbuffer

    def _save(self, filename, content):
        path = os.path.join(self.bucket_name, filename)
        with cloudstorage.open(
            path, 'w',
            content_type=mimetypes.guess_type(filename)[0],
            options=HEADERS) as handle:
            handle.write(content.read())
        return os.path.join(self.bucket_name, filename)

    def created_time(self, filename):
        filestat = cloudstorage.stat(os.path.join(self.bucket_name, filename))
        return datetime.datetime.fromtimestamp(filestat.st_ctime)

    def path(self, name):
        print "#### get path", name
        return name

    def listdir(self, path):
        if path:
            realpath = os.path.join(self.bucket_name, path)
        else:
            realpath = self.bucket_name
        return ([], [obj.filename[len(self.bucket_name)+1:]
            for obj in cloudstorage.listbucket(realpath)])

    def url(self, filename):
        print "#### get url", filename
        try:
            key = blobstore.create_gs_key('/gs' + os.path.join(self.bucket_name, filename))
            url = images.get_serving_url(key, size=DEFAULT_SIZE, secure_url=SECURE)
        except Exception as exp:
            logging.error('Exception generating url to %s: %s', filename, exp)
            u = urlparse.urlsplit(filename)
            url = 'https://storage.googleapis.com{path}'.format(path=u.path)
        return url
