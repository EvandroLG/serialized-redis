from unittest import TestCase, mock
from serialized_redis import SerializedRedis
import redis
import pickle


class TestSerializedRedis(TestCase):
	def setUp(self):
		self.redis = SerializedRedis()

	def tearDown(self):
		self.redis.delete('mimi')

	def verify_result(self, expected_value):
		self.redis.set('mimi', expected_value)
		self.assertEqual(self.redis.get('mimi'), expected_value)

	@mock.patch('pickle.dumps')
	def test_set_method_should_call_method_dumps_from_pickle_with_correct_parameter(self, *args):
		self.redis.set('mimi', [1, 2, 3])

		pickle.dumps.assert_any_call([1, 2, 3])
		self.assertTrue(pickle.dumps.call_count == 1)

	@mock.patch('redis.Redis.get')
	@mock.patch('pickle.loads')
	def test_get_method_should_call_method_loads_from_pickle(self, *args):
		self.redis.get('mimi')
		self.assertTrue(pickle.loads.call_count == 1)

	def test_get_method_should_return_a_list_serialized(self):
		self.verify_result([1, 2, 3])

	def test_get_method_should_return_a_dict_seralized(self):
		self.verify_result({'name': 'Evandro'})

	def test_get_method_should_return_a_string(self):
		pass