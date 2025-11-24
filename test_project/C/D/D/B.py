E=int
B=property
import abc as A
class D(metaclass=A.ABCMeta):
	@B
	@A.abstractmethod
	def name(self):0
	@B
	@A.abstractmethod
	def key_sizes(self):0
	@B
	@A.abstractmethod
	def key_size(self):0
class C(D):
	key:bytes
	@B
	@A.abstractmethod
	def block_size(self):0