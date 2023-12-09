from PyQt6.QtWidgets import *
from basvurular import Ui_MainWindow
import gspread

class basvurular_sayfasi(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.basvuru = Ui_MainWindow()
        self.basvuru.setupUi(self)
        self.basvuru.TercihlerEkraniButtonBas.clicked.connect(self.TercihlerSayfasinaGit)
        self.basvuru.tumBasvurularButton.clicked.connect(self.veriyiCekVeTabloyaEkle)
        self.basvuru.araButtonbas.clicked.connect(self.searchData)
        self.basvuru.MentorTanimliButton.clicked.connect(self.mentorTanimliButtonClicked)
        self.basvuru.MentorTanimsizButton.clicked.connect(self.mentorTanimsizButtonClicked)

    def get_spreadsheet_data(self, spreadsheet_name, worksheet_index):
        credentials = 'wrherecrmproject-af4aa86d1e43.json'
        gc = gspread.service_account(filename=credentials)
        spreadsheet = gc.open(spreadsheet_name)
        worksheet = spreadsheet.get_worksheet(worksheet_index)
        return worksheet.get_all_values()


    def TercihlerSayfasinaGit(self):
        from tercihler_sayfasi import tercih_sayfasi
        self.close()
        self.tercih = tercih_sayfasi()
        self.tercih.show()

    def veriyiCekVeTabloyaEkle(self):
        all_values = self.get_spreadsheet_data('Basvurular',0)

        # Verileri tabloya ekle
        self.basvuru.tableWidgetB.setColumnCount(len(all_values[0]))
        self.basvuru.tableWidgetB.setHorizontalHeaderLabels(all_values[0])
        self.basvuru.tableWidgetB.setRowCount(len(all_values) - 1)

        for i, row in enumerate(all_values[1:]):
                for j, value in enumerate(row):
                    
                    item = QTableWidgetItem(str(value))
                    self.basvuru.tableWidgetB.setItem(i, j, item)

    def searchData(self):

        search_text = self.basvuru.lineEditBas.text().lower()

        all_values = self.get_spreadsheet_data('Basvurular', 0)

        filtered_values = [row for row in all_values if search_text in str(row[1]).lower()]
            # Update the table with filtered data
        self.basvuru.tableWidgetB.setRowCount(len(filtered_values))

        for i, row in enumerate(filtered_values):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.basvuru.tableWidgetB.setItem(i, j, item)

    def mentorTanimliButtonClicked(self):

        mentor_column_index = 20

        all_values = self.get_spreadsheet_data('Basvurular', 0)

        mentor_rows = [row for row in all_values if row[mentor_column_index] == 'OK']

        # Update the table with filtered data
        self.basvuru.tableWidgetB.setRowCount(len(mentor_rows))
        self.basvuru.tableWidgetB.setHorizontalHeaderLabels(all_values[0])
        self.basvuru.tableWidgetB.setColumnCount(len(all_values[0]))  # to keep the same number of columns
        

        for i, row in enumerate(mentor_rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.basvuru.tableWidgetB.setItem(i, j, item)

    def mentorTanimsizButtonClicked(self):

        mentor_column_index = 20

        all_values = self.get_spreadsheet_data('Basvurular',0)

        mentor_rows = [row for row in all_values if row[mentor_column_index] != 'OK']

        # Update the table with filtered data
        self.basvuru.tableWidgetB.setRowCount(len(mentor_rows))
        self.basvuru.tableWidgetB.setHorizontalHeaderLabels(all_values[0])
        self.basvuru.tableWidgetB.setColumnCount(len(all_values[0]))  # to keep the same number of columns

        for i, row in enumerate(mentor_rows[1:]):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.basvuru.tableWidgetB.setItem(i, j, item)