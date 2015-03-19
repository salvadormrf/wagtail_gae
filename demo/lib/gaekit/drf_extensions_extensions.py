import datetime

from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.utils.encoding import force_text

from rest_framework_extensions.key_constructor.constructors import DefaultListKeyConstructor
from rest_framework_extensions.key_constructor.bits import KeyBitBase, QueryParamsKeyBit

class ModelsKeyBit(KeyBitBase):
    def get_data(self, params, **kwargs):
        value = cache.get(params, None)
        if not value:
            value = datetime.datetime.utcnow()
            cache.set(params, value=value)
        return force_text(value)

class FeedListKeyConstructor(DefaultListKeyConstructor):
    def __init__(self, params, *args, **kwargs):
        super(FeedListKeyConstructor, self).__init__(params)
        self.models = params.get('models', [])
        self.connect_signals()
        self.bits['models'] = ModelsKeyBit(params=self.models)

    def update_cache_key(self, sender=None, instance=None, raw=False, *args, **kwargs):
        if sender in self.models and not raw:
            cache.set(str(self.models), datetime.datetime.utcnow())

    def connect_signals(self):
        for model in self.models:
            post_save.connect(receiver=self.update_cache_key, sender=model)
            post_delete.connect(receiver=self.update_cache_key, sender=model)