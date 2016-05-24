class PriorityQueueBase(object):

	# --- item class ---
	class Item(object):
		# key is the priority, value is the actual value you want to store
		__slots__ = ['key','value']

		def __init__(self,key,value):
			self.key = key
			self.value = value

		def __lt__(self,other):
			return self.key < other.key

from chapter7 import LinkedDeque

class PriorityQueueUnsorted(PriorityQueueBase):
	def __init__(self):
		self.holder = LinkedDeque()

	def __len__(self):
		return len(self.holder)

	def is_empty(self):
		return self.holder.is_empty()

	def add(self, key, value):
		item = self.Item(key,value)
		self.holder.insert_last(item)

	def min(self):
		''' peak on the mininum value item
			This is O(n) time O(1) space
		'''
		if self.is_empty():
			raise Exception('Nothing inside')

		m = self.holder.peak_first()
		for each in self.holder:
			if each.key < m.key:
				m = each
		return m

	def pop_min(self):
		''' read and remove and return the min key item '''
		if self.is_empty():
			raise Exception('Nothing inside')

		m = self.holder.peak_first()
		for each in self.holder:
			if each.key < m.key:
				m = each
		return m