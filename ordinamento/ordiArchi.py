Ordinare archi:
def get_top_edges(self):
        sorted_edges = sorted(self._grafo.edges(data=True), key=lambda edge: edge[2].get('weight'), reverse=True)
        return sorted_edges[0:5]
Output:
        for edge in top_edges:
            self._view.txt_result1.controls.append(ft.Text(f"{edge[0].id} -> {edge[1].id} | weight = {edge[2]['weight']}"))
