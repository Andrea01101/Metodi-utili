Distanza:
dist = distance((l1.Latitude, l1.Longitude), (l2.Latitude, l2.Longitude)).km

Archi uscenti:
    def get_node_max_uscenti(self):
        sorted_nodes = sorted(self._graph.nodes(), key=lambda n: self._graph.out_degree(n), reverse=True)
        result = []
        for i in range(min(len(sorted_nodes), 5)):
            peso_tot = 0.0
            for e in self._graph.out_edges(sorted_nodes[i], data=True):
                peso_tot += float(e[2].get("weight"))
            result.append((sorted_nodes[i], self._graph.out_degree(sorted_nodes[i]), peso_tot))
        return result
Controller
sorted_nodes = self._model.get_node_max_uscenti()
        n_nodi = min(len(sorted_nodes),5)
        self._view.txt_result1.controls.append(ft.Text(f"\nI {n_nodi} nodi col maggior numero di archi uscenti sono:"))
        for i in range(n_nodi):
            self._view.txt_result1.controls.append(ft.Text(f"{sorted_nodes[i][0]} | "
                                                           f"num. archi uscenti: {sorted_nodes[i][1]}  | "
                                                           f"peso tot.: {sorted_nodes[i][2]}"))
