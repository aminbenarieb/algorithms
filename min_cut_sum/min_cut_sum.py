import random
# hw_filename = "_f370cd8b4d3482c940e4a57f489a200b_kargerMinCut.txt"
hw_filename = "test.txt"

class Graph:
	@classmethod
	def min_cut_sum(cls, adj_vertices):
		# result = 0
		n_v = len(adj_vertices)
		rand_v1_ind = random.randint(0, n_v-1)
		v1 = adj_vertices[rand_v1_ind]

		m_v1 = v1.len()
		rand_v2_ind = random.randint(1, m_v1-1)
		v2 = v1[rand_v2_ind]

		print(print_adj_list_arr(adj_vertices))
		print("\n")
		print(v1.label, v2.label)
		print("\n")
		# Graph.combine(v1,v2)
		print(print_adj_list_arr(adj_vertices))
		# for node in adj_vertices:
		# return result

	@classmethod
	def combine(cls, node1, node2):
		node = node2.next
		node1.append(node)
		# node1.delete_self_loops()
		
class Node:
	def __init__(self, next, label):
		self.next = next
		self.label = label
	def len(self):
		len = 0
		node = self
		while node != None:
			len += 1 
			node = node.next
		return len
	def __delitem__(self, key):
		self[key-1] = self[key+1]
	def __getitem__(self, key):
		node = self
		i = 0
		while node != None and i != key:
			node = node.next
			i += 1
		return node
	def __setitem__(self, key, value):
		self[key] = value
	def append(self, new_node):
		node = self
		while node.next != None:
			node = node.next
		node.next = new_node


	def delete_self_loops(self):
		if self == None:
			return

		curr = self
		next = self.next
		while next != None:
			if next == self:
				curr.next = next.next
				next = curr.next
			else:
				curr = curr.next
				next = next.next

def print_adj_list_arr(adj_vertices):
	for node in adj_vertices:
		adj_vertices = node.label
		adj_node = node.next
		while adj_node != None:
			adj_vertices += " -> "+str(adj_node.label)
			adj_node = adj_node.next

		print(adj_vertices, adj_node)

def adj_list_arr_from_file(filepath):
	result = []
	lists =  [number for number in [line.rstrip('\n').split("\t") for line in open(filepath)]]
	for adj_vertices in lists:
		node = Node(None, adj_vertices[0])
		result.append(node)
		for (index, label) in enumerate(adj_vertices):
			if 0 < index < len(adj_vertices) - 1:
				nextNode = Node(None, label)
				node.next = nextNode
				node = nextNode

	return result


print("\n\n")
adj_vertices = adj_list_arr_from_file(hw_filename)
Graph.min_cut_sum(adj_vertices)
# print(min_cut_sum(adj_vertices))