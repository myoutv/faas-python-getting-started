from PyQt5.QtWidgets import (
    QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton
)
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion des Documents Commerciaux")
        self.setGeometry(100, 100, 800, 600)

        # Tableau principal
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Type", "Numéro", "Client", "Date"])
        self.table.setRowCount(10)  # Exemple : 10 lignes

        # Boutons d'action
        self.add_button = QPushButton("Créer un Document")
        self.edit_button = QPushButton("Modifier")
        self.delete_button = QPushButton("Supprimer")

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.add_button)
        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)

        # Container principal
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Connexions des boutons
        self.add_button.clicked.connect(self.create_document)
        self.edit_button.clicked.connect(self.edit_document)
        self.delete_button.clicked.connect(self.delete_document)

    def create_document(self):
        print("Créer un nouveau document")

    def edit_document(self):
        print("Modifier un document sélectionné")

    def delete_document(self):
        print("Supprimer un document sélectionné")
