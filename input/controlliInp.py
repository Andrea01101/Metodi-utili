Controlli su input:
soglia = self._view.casella_testo.value
try:
    sogliaInt = int(soglia)
except ValueError:
self._view.txt_result2.controls.clear()
self._view.txt_result2.controls.append(ft.Text("Inserire un valore intero"))
self._view.update_page()
return