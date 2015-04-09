from unittest import TestCase, mock
from serialized_redis import SerializedRedis
import redis
import pickle


class TestSerializedRedis(TestCase):
    def setUp(self):
        self.redis = SerializedRedis()

    def tearDown(self):
        self.redis.delete('mimi')

    def verify_result(self, input_value, expected_value):
        self.redis.set('mimi', input_value)
        self.assertEqual(self.redis.get('mimi'), expected_value)

    @mock.patch('pickle.dumps')
    def test_set_method_should_call_method_dumps_from_pickle_with_correct_parameter(self, *args):
        self.redis.set('mimi', [1, 2, 3])

        pickle.dumps.assert_any_call([1, 2, 3])
        self.assertTrue(pickle.dumps.call_count == 1)

    @mock.patch('pickle.dumps')
    def test_rpushx_method_should_call_method_dumps_from_pickle_with_correct_parameter(self, *args):
        self.redis.rpushx('mimi', [1, 2, 3])

        pickle.dumps.assert_any_call([1, 2, 3])
        self.assertTrue(pickle.dumps.call_count == 1)

    @mock.patch('redis.Redis.get')
    @mock.patch('pickle.loads')
    def test_get_method_should_call_method_loads_from_pickle(self, *args):
        self.redis.set('mimi', [1, 2, 3])
        self.redis.get('mimi')
        self.assertTrue(pickle.loads.call_count == 1)

    def test_get_method_should_return_a_list_serialized(self):
        self.verify_result([1, 2, 3], [1, 2, 3])

    def test_get_method_should_return_a_dict_seralized(self):
        self.verify_result({'name': 'Evandro'}, {'name': 'Evandro'})

    def test_get_method_should_return_a_string_as_a_byte(self):
        self.verify_result('Evandro', b'Evandro')

    def test_get_method_should_return_a_number_as_a_byte(self):
        self.verify_result(1234, b'1234')

    #@mock.patch('redis.Redis.rpush')
    def verify_lrange_method(self, key, first_datas, last_datas, instance):
        return
        self.redis.rpush(key, first_datas)
        self.redis.rpush(key, last_datas)

        result = self.redis.lrange(key, 0, 1)

        is_type_valid = isinstance(result[0], instance)
        expected_size = len(result)

        self.assertTrue(is_type_valid)
        self.assertEqual(expected_size, 2)
        self.assertEqual(result, [ first_datas, last_datas ])

    def test_lrange_method_should_return_two_serialized_list(self):
        self.verify_lrange_method('animals', ['dog', 'cat'], ['elephant', 'alligator'], list)

    def test_lrange_method_should_return_two_serialized_dict(self):
        self.verify_lrange_method('people', { 'name': 'Evandro' }, { 'name': 'Carmen' }, dict)
