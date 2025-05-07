class MultipleDatabaseConnectionError(Exception):
    pass

class DatabaseConnection:
    __instance = None
    def __init__(self, database_name):
        if DatabaseConnection.__instance is None:
            DatabaseConnection.__instance = self
            self.database_name = database_name
        else:
            raise MultipleDatabaseConnectionError
    def __repr__(self):
        return f"Соединние с БД {self.database_name}"
    
conn = DatabaseConnection("account_info.db")

print(conn)

print(DatabaseConnection._DatabaseConnection__instance)

conn1 = DatabaseConnection("accousnt_info.db")
