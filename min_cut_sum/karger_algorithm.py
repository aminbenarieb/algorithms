import random, copy

hw_filename = "_f370cd8b4d3482c940e4a57f489a200b_kargerMinCut.txt"
# hw_filename = "test.txt"

data = open(hw_filename,"r")
G = {}
for line in data:
    lst = [int(s) for s in line.split()]
    G[lst[0]] = lst[1:]   

def choose_random_key(G):
    v1 = random.choice(list(G.keys()))
    v2 = random.choice(list(G[v1]))
    return v1, v2

def karger(G):

    while len(G) > 2:
        # chosing random two vertices
        v1, v2 = choose_random_key(G)

        # adding v2 incident vertices to v1
        G[v1].extend(G[v2])

        # for every vertice that incident to v2 
        for x in G[v2]:
            G[x].remove(v2) # removing v2 from x-vertice edges
            G[x].append(v1) # adding v2 connection as v1  to x-vertice

        # removing self-loops
        while v1 in G[v1]:
            G[v1].remove(v1)

        # finally deleting v2 from graph
        del G[v2]

    length = [len(G[key]) for key in G.keys()]
    return length[0]

def operation(n):
    i = 0
    count = len(G) - 1
    while i < n:
        copied_graph = copy.deepcopy(G)
        min_cut = karger(copied_graph)
        if min_cut < count:
            count = min_cut
        i = i + 1
    return count

print(operation(10))