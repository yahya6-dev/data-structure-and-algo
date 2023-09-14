def  search(G,start,goal):
	current = start
	stack = Stack(start)
	visited = set([current])

	while not stack.isEmpty():
		current = stack.pop()
		visited.add(current)
		if current == goal:
			 return True
		for v in G[current]:
			if v not in visited:
				stack.push(v)
	return False
