Cammini:
1)Esiste un percorso?

    def esistePercorso(self, v0, v1):
        connessa = nx.node_connected_component(self._grafo, v0)
        if v1 in connessa:
            return True
	return False

2)Trovare il percorco:

2.1)def trovaCamminoD(self, v0, v1):
	return nx.dijkstra_path(self._grafo, v0, v1)

2.2)def trovaCamminoBFS(self, v0, v1):
        tree = nx.bfs_tree(self._grafo, v0)
        if v1 in tree:
            print(f"{v1} è presente nell'albero di visita BFS")
        path = [v1]

        while path[-1] != v0:
            path.append(list(tree.predecessors(path[-1]))[0])

        path.reverse()
        return path