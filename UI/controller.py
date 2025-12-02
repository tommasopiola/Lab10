import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        # TODO
        try:
            input_val = self._view.guadagno_medio_minimo.value
            if not input_val:
                self._view.show_alert("Inserire un valore numerico.")
                return

            threshold = float(input_val)
        except ValueError:
            self._view.show_alert("Inserire un valore numerico valido.")
            return

        self._model.costruisci_grafo(threshold)

        n_nodes = self._model.get_num_nodes()
        n_edges = self._model.get_num_edges()
        edges_data = self._model.get_all_edges()

        self._view.lista_visualizzazione.controls.clear()

        self._view.lista_visualizzazione.controls.append(
            ft.Text(f"Numero di Hubs: {n_nodes}")
        )

        self._view.lista_visualizzazione.controls.append(
            ft.Text(f"Numero di Tratte: {n_edges}")
        )

        for u, v, data in edges_data:
            weight = data['weight']
            row_txt = f"{u} -> {v} -- guadagno medio per spedizione: € {weight:.2f}"
            self._view.lista_visualizzazione.controls.append(ft.Text(row_txt))

        self._view.update()
