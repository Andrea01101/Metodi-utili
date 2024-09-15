for row in cursor:
    result.append(row["attributo del select"])

for row in cursor:
    result.append(Nome_Classe(**row))

DAO:
for row in cursor:
    result.append(Neightbours(idMap[row["s1"]], idMap[row["s2"]], row["tot"]))  # nodo1,nodo2,peso
Model:
neight = DAO.getAllEdges(s, y, self._idMap)
for n in neight:
    self._grafo.add_edge(n.state1, n.state2, weight=n.tot)

Per i PESI che vanno SOMMATI:
    def getWeight(self):
        lista = []
        for v in self._grafo.nodes:
            somma = 0
            for n in list(self._grafo.neighbors(v)):
                somma += self._grafo[v][n]["weight"]
            lista.append((v, somma))
        return lista

DAO:
for row in cursor:
    result.append((row['Gene1'], row['Gene2'], row['Expression_Corr']))
Model:
allConnessioni = DAO.getAllEdges()
for g1, g2, p in allConnessioni:
    self._graph.add_edge(g1, g2, weight=p)

DAO:
for row in cursor:
    result[idMap[row["ID"]]] = row["totSalary"] #chiave oggetto team e valore salario
Model:
salary = DAO.getSalaryOfTeams(year, self._idMap)
for e in self._grafo.edges:
    self._grafo[e[0]][e[1]]["weight"] = salary[e[0]] + salary[e[1]]

self._idMap = {}
for s in nodi:
    self._idMap[s.id] = s

Accedere al peso di un arco: self._grafo[v1][v2]["weight"]