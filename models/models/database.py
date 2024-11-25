import sqlite3

class Database:
    def __init__(self, db_name="documents.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            number TEXT,
            client TEXT,
            date TEXT
        )
        """
        self.connection.execute(query)
        self.connection.commit()

    def add_document(self, doc):
        query = "INSERT INTO documents (type, number, client, date) VALUES (?, ?, ?, ?)"
        self.connection.execute(query, (doc.doc_type, doc.number, doc.client, doc.date))
        self.connection.commit()
