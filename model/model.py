from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        # TODO
        self.G.clear()
        # Ottengo i dati dal DAO (Hub e Archi)
        all_hubs = DAO.get_all_hubs()
        all_connessioni = DAO.get_all_connessioni()

        # Aggiungo tutti i nodi al grafo G
        self.G.add_nodes_from(all_hubs)

        # Creo una mappa per recuperare l'oggetto Hub partendo dal suo ID
        # id_map[1] -> Oggetto Hub(id=1, ...)
        id_map ={hub.id: hub for hub in all_hubs}

        for u_id, v_id, peso in all_connessioni:
            peso_float = float(peso)

            if peso_float >= threshold:
                nodo_u=id_map[u_id]
                nodo_v=id_map[v_id]

                self.G.add_edge(nodo_u, nodo_v, weight=peso_float)

    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        return self.G.number_of_edges()

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        return self.G.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        return self.G.edges(data=True)
