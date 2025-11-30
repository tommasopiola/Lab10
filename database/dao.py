from database.DB_connect import DBConnect
from model.hub import Hub

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO
    @staticmethod
    def get_all_hubs():
        conn = DBConnect.get_connection()
        result = []

        if conn is None:
            print("Errore di connesione al database")
            return result

        cursor = conn.cursor(dictionary=True)
        query = '''SELECT * FROM hub'''

        cursor.execute(query)

        for row in cursor:
            result.append(Hub(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_connessioni():
        # Raggruppo le spedizioni AB e BA insieme
        # Restituisco una lista di tuple(id_partenza, id_arrivo, peso_medio).

        conn = DBConnect.get_connection()
        result = []

        if conn is None:
            print("Errore di connesione al database")
            return result

        cursor = conn.cursor(dictionary=True)
        query = ('''SELECT LEAST (id_hub_origine, id_hub_destinazione) as id1,
                           GREATEST (id_hub_origine, id_hub_destinazione) as id2,
                           AVG(valore_merce) as peso
                 FROM SPEDIZIONE
                 GROUP BY id1, id2''')
        cursor.execute(query)

        for row in cursor:
            result.append((row['id1'], row['id2'], row['peso']))

        cursor.close()
        conn.close()
        return result