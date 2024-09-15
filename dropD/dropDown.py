Riempimento Dropdown:
1)for a in years:
    self._view.nome_dropdown.options.append(ft.dropdown.Option(a))

2)    def fillDDYear(self):
        years = self._model.getYears() #lista interi
        yearsDD = map(lambda x: ft.dropdown.Option(x), years) #applico una funzione
        self._view._ddAnno.options = yearsDD
        self._view.update_page()

    def handleDDYearSelection(self, e):
	self._view.ddSquadra.options.clear()
        self._view.ddSquadra.value = None
        teams = self._model.getTeamsOfYears(self._view._ddAnno.value)
        for t in teams:
            self._view._txtOutSquadre.controls.append(ft.Text(f"{t.teamCode}"))
            self._view._ddSquadra.options.append(ft.dropdown.Option(
                data = t,
                text = t.teamCode,
                on_click = self.readDDTeams
            ))
        self._view.update_page()
self._ddAnno = ft.Dropdown(label="Anno", width=200, alignment=ft.alignment.top_left, on_change=self._controller.handleDDYearSelection)

3)Non ho direttamente ciò che deve riempire il dropdown
nodes = self._model.getNodes()
        nodes.sort(key=lambda x: x.Title)
        listDD = map(lambda x: ft.dropdown.Option(data=x,
                                                  text=x.Title,
                                                  on_click=self.getSelectedAlbum), nodes)
        self._view._ddAlbum.options.extend(listDD)
        self._view.update_page()

        self._view.update_page()

    def getSelectedAlbum(self, e):
        if e.control.data is None:
            self._choiceAlbum = None
        else:
            self._choiceAlbum = e.control.data

# verifico che il primo nodo dell'arco sia già stato aggiunto
        for row in cursor:
            if row["a1"] in idMap and row["a2"] in idMap:  # solo se esistono appendo
                result.append((idMap[row["a1"]], idMap[row["a2"]]))

for s in shapes:
            self._view.ddstate.options.append(ft.dropdown.Option(key=s.id, text=s.name))