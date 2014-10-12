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

    def rpush(self, key, value):
        self._execute_command(key, value, super(Redis, self).rpush)

    def lrange(self, key, start, end):
        value_list = super(Redis, self).lrange(key, start, end)
        is_empty = len(value_list) == 0

        if is_empty:
            return value_list

        def make_result(value):
            try:
                return pickle.loads(value)
            except:
                pass

            return value

        result = [make_result(value) for value in value_list]

        return result
