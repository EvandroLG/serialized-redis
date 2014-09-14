from redis import Redis
import pickle


class SerializedRedis(StrictRedis):
	def set(self, key, value):
		super(SerializedRedis, self).set(key, pickle.dumps(value))

	# def get(self, key):
		# pass
		# super()
