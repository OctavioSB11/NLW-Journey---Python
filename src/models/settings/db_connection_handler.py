import sqlite3
from sqlite3 import Connection

class DbConnectionHandler: #cria uma classe para realizar as conexoes com banco de dados
    def __init__(self) -> None:
        self.__connection__string = "storage.db"
        self.__conn = None

    def connect(self) -> None:
        conn = sqlite3.connect(self.__connection__string, check_same_thread= False)
        self.__conn = conn

    def get_connection(self) -> Connection:
        return self.__conn
    
db_connection_handler = DbConnectionHandler() #como usamos apeas uma conexao, fazemos o tratamento no ultimo def acima
    