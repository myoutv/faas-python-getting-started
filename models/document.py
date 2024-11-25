class Document:
    def __init__(self, doc_type, number, client, date):
        self.doc_type = doc_type
        self.number = number
        self.client = client
        self.date = date

    def to_dict(self):
        return {
            "type": self.doc_type,
            "number": self.number,
            "client": self.client,
            "date": self.date,
        }
