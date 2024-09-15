Componente connessa e vicini:
    def getConnessaDetails(self, v0):
        conn = nx.node_connected_component(self._graph, v0)
        durataTOT = 0
        for album in conn:
            durataTOT += toMinutes(album.totD)

        return len(conn), durataTOT

    A)def getSortedNeighbors(self, v0):
        vicini = self._grafo.neighbors(v0)
        viciniTuple = []
        for v in vicini:
            viciniTuple.append((v, self._grafo[v0][v]["weight"]))
        viciniTuple.sort(key=lambda x: x[1], reverse=True)
        return viciniTuple

    B)  def getNodesMostVicini(self):
        #trovo i vicini
        listTuples = []
        for v in self._nodes:
            listTuples.append((v, len(list(self._graph.neighbors(v)))))
        listTuples.sort(key=lambda x: x[1], reverse=True)

        # result1 = list(filter(lambda x: x[1] == listTuples[0][1] , listTuples))

        result2 = [x for x in listTuples if x[1] == listTuples[0][1]]

        return result2

    def get_largest_connessa(self):
        conn = list(nx.weakly_connected_components(self._grafo))
        conn.sort(key=lambda x: len(x), reverse=True) #ordinamento
        return conn[0]