#namedtuple 可以使用属性而不是索引引用tuple的元素
from collections import namedtuple
point = namedtuple('point',['x','y'])
p = point(1,2)
print(p.x)
print(p.y)

#deque 高效实现插入删除操作的双向列表，适合队列和栈
from collections import deque
ls = ['a','b','c']
q = deque(ls)
q.append('x')
q.popleft()
q.appendleft('y')
print(q)

#defaultdict      使字典被引用的键不存在时返回默认值
from collections import defaultdict
dd = defaultdict(lambda:0)
print(dd)
dd['key1'] = 'abc'
print(dd['key1']) #存在
print(dd['key2']) #不存在返回默认值
print(dd)

#OrderedDict 保持key的顺序
from collections import OrderedDict
d = dict([('a',1),('b',2),('c',3)])
print(d)
od = OrderedDict([('a',1),('b',2),('c',3)])
print(od)
odd = OrderedDict()
odd['z'] = 1 
odd['x'] = 2
odd['y'] = 3
print(list(odd.keys())) #按照插入顺序排序

#先进先出的字典
from collections import OrderedDict

class luod(OrderedDict):

	def __init__(self,cap):
		super(luod,self).__init__()
		self._cap = cap

	def __setitem__(self,key,value):
		containskey = 1 if key in self else 0 
		if len(self) - containskey >= self.cap:
			last = self.popitem(last=Flase)
			print('remove:',last)
		if containskey:
			del self[key]
			print('set:',(key,value))
		else:
			print('add:',(key,value))
		OrderedDict.__setitem__(self,key,value)

#计数器
from collections import Counter
c = Counter()
for x in 'prgra232^&*=mdaf23da':
	c[x]+=1
print(c)

