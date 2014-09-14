#!/usr/bin/python
# -*- coding: utf-8 -*-

# SerializedRedis
# author: Evandro Leopoldino Gonçalves <evandrolgoncalves@gmail.com>
# https://github.com/evandrolg
# License: MIT

from redis import Redis
import pickle


class SerializedRedis(Redis):
    def set(self, key, value):
        is_list_or_dict = isinstance(value, list) or isinstance(value, dict)

        if is_list_or_dict:
            super(Redis, self).set(key, pickle.dumps(value))
            return

        super(Redis, self).set(key, value)

    def get(self, key):
        value = super(Redis, self).get(key)

        try:
            return pickle.loads(value)
        except:
            pass

        return value
