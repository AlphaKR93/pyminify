import abc
class C(metaclass=abc.ABCMeta):
	@property
	@abc.abstractmethod
	def name(self):0