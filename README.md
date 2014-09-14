# SerializedRedis
A solution to have lists and dictionaries serialized using redis-py.


**Examples**
```python
    from serialized_redis import SerializedRedis

    redis = SerializedRedis()
    redis.set('datas', { 'name': 'Evandro', 'age:': 27 })
    type(redis.get('datas')) # It will return a dictionary
```