#!/usr/bin/python3 

import sys

with open(sys.argv[1]) as input_:

	nodes = set(range(1, int(input_.readline().strip())+1))
	edges = dict()
	subtree_idx = 1
	subtree_loc = dict()

	for line in input_:
		edge = tuple(sorted(list(map(int, line.strip().split(" ")))))
		a, b = edge
		is_updated = False
		loc_a = subtree_loc.get(a)
		loc_b = subtree_loc.get(b)
		if loc_a and loc_b:
			edges[loc_a].update(edges[loc_b])
			for node in edges[loc_b]:
				subtree_loc[node] = loc_a
			del edges[loc_b]
		elif not loc_a and not loc_b:
			edges[subtree_idx] = set(edge)
			subtree_loc[a] = subtree_idx
			subtree_loc[b] = subtree_idx
			subtree_idx += 1
		else:
			loc_to_add = loc_a if loc_a else loc_b
			edges[loc_to_add].update(set(edge))
			subtree_loc[a] = loc_to_add
			subtree_loc[b] = loc_to_add

not_found_nodes = nodes - set.union(*edges.values())
print(len(edges) + len(not_found_nodes) - 1)
