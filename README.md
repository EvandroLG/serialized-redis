# SerializedRedis
A solution to have lists and dictionaries serialized using redis-py.

**Instalation**
To install serialized_redis, simply:
```shell
	pip install serialized-redis
```


**Examples**
```python
    from serialized_redis import SerializedRedis

    redis = SerializedRedis()
    redis.set('datas', { 'name': 'Evandro', 'age:': 27 })
    type(redis.get('datas')) # It will return a dictionary
```