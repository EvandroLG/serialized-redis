# SerializedRedis
A solution to have lists and dictionaries serialized using redis-py.

**Examples**
```python
    redis = SerializedRedis()
    redis.set('datas', { 'name': 'Evandro', 'age:': 27 })
    type(redis.get('datas')) # It will return a dictionary
```