#!/usr/bin/python
# -*- coding: utf-8 -*-

# SerializedRedis
# author: Evandro Leopoldino Gonçalves <evandrolgoncalves@gmail.com>
# https://github.com/evandrolg
# License: MIT

from redis import Redis
import pickle


class SerializedRedis(Redis):
    def _execute_command(self, key, value, method):
        is_list_or_dict = isinstance(value, list) or isinstance(value, dict)

        if is_list_or_dict:
            method(key, pickle.dumps(value))
            return

        method(key, value)

    def set(self, key, value):
        self._execute_command(key, value, super(Redis, self).set)

    def get(self, key):
        value = super(Redis, self).get(key)

        try:
            return pickle.loads(value)
        except:
            pass

        return value

    def rpushx(self, key, value):
        self._execute_command(key, value, super(Redis, self).rpushx)

    # def rpush(self, key, *values):
    #     pass

    # def lrange(self, key, start, end):
        # import pdb; pdb.set_trace()
