#
# HashOpenAddr 클래스 선언
#
class HashOpenAddr:
	def __init__(self, size= 150000):
			self.size = size
			self.keys = [None]*self.size
			self.values = [None]*self.size
	def __str__(self):
			s = ""
			for k in self:
					if k == None:
							t = "{0:5s}|".format("")
					else:
							t = "{0:-5d}|".format(k)
					s = s + t
			return s
	def __iter__(self):
			for i in range(self.size):
					yield self.keys[i]

	def find_slot(self, key):
		i = self.hash_function(key)
		start = i
		while (self.keys[i] != None) and (self.keys[i] !=key):
			i = (i + 1) % self.size
			if i == start: 
				return "FULL"
		return i

	def set(self, key, value=None):
		i = self.find_slot(key)
		if i == "FULL":
			return None
		if self.keys[i] != None:
			self.values[i] = value
		else:
			self.keys[i] = key 
			self.values[i] = value
		return key 

	def hash_function(self, key):
			return key % self.size

	def remove(self, key):
		i = self.find_slot(key)
		if self.keys[i] == None:
			return None
		j = i
		while True:
			self.keys[i] = None
			while True:
				j = (j + 1) % self.size
				if self.keys[j] == None:
					return key
				a = self.keys[j]
				k = self.hash_function(a)
				if not (i < k <= j or j< i< k or k <= j < i):
					break
			self.keys[i] = self.keys[j]
			i = j

	def search(self, key):
		i = self.find_slot(key)
		if self.keys[i] != None:
			return self.keys[i]
		else:
			return None

	def __getitem__(self, key):
			return self.search(key)
	def __setitem__(self, key, value):
			self.set(key, value)


# 입력
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
#
# 코드 (hash table을 이용)
#

H1 = HashOpenAddr()
H2 = HashOpenAddr()
W = list()
L = list()

for i in A:
	m = H1.find_slot(i)
	if H1.keys[m] != None:
		H1.set(i, H1.values[m]+1)
	else:	H1.set(i, 0)
	H2.set(i)

for i in B:
	m = H1.find_slot(i)
	b = H2.remove(i)
	if b != None:
		L.append(b)
	if H1.keys[m] != None:
		l = H1.values[m]
		if l == 0:
			W.append(H1.remove(i))
		else:
			W.append(H1.keys[m])
			H1.set(i, l-1) 

W = list(map(str, W))
strW = " ".join(W)
print(strW)

L = list(map(str, L))
strL =" ".join(L)
print(strL)
	