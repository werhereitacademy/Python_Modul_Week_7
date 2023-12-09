from PyQt6.QtWidgets import *
from mulakatlar import Ui_MulakatlarSayfasi
import gspread

class mulakatlar_sayfasi(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.mulakat=Ui_MulakatlarSayfasi()
        self.mulakat.setupUi(self)
        self.mulakat.TercihlerEkraniButtonMul.clicked.connect(self.TercihlerSayfasinaGit)
       # self.mulakat.tableWidgetMul = Ui_MulakatlarSayfasi()
       # self.loaddata()
        self.mulakat.pushButton_4.clicked.connect(self.searchData)
        self.mulakat.ProjeGelenButton.clicked.connect(self.projeGelen)
        self.mulakat.ProjeGondButton.clicked.connect(self.projeGiden)
        self.mulakat.tumMulButton.clicked.connect(self.tabloyaEkle)   
        #self.veriyiCekVeTabloyaEkle()
    def tabloyaEkle(self):
        credentials = 'wrherecrmproject-af4aa86d1e43.json'
        gc = gspread.service_account(filename=credentials)
        spreadsheet = gc.open('Mulakatlar')
        worksheet = spreadsheet.get_worksheet(0)
        all_values = worksheet.get_all_values()
        # Verileri tabloya ekle
        self.mulakat.tableWidgetMul.setColumnCount(len(all_values[0]))
        self.mulakat.tableWidgetMul.setHorizontalHeaderLabels(all_values[0])
        self.mulakat.tableWidgetMul.setRowCount(len(all_values)-1)

        for i, row in enumerate(all_values[1:]):
                for j, value in enumerate(row):
                    #self.mulakat.tableWidgetMul.horizontalHeader().setVisible(False)
                    item = QTableWidgetItem(str(value))
                    self.mulakat.tableWidgetMul.setItem(i, j, item)
    def TercihlerSayfasinaGit(self):
        from tercihler_sayfasi import tercih_sayfasi
        self.close()
        self.tercih=tercih_sayfasi()
        self.tercih.show()
    def searchData(self):  
        search_text = self.mulakat.lineEdit.text().lower()
        credentials = 'wrherecrmproject-af4aa86d1e43.json'
        gc = gspread.service_account(filename=credentials)
        spreadsheet = gc.open('Mulakatlar')
        worksheet = spreadsheet.get_worksheet(0)
        all_values = worksheet.get_all_values()
        filtered_values = [row for row in all_values if search_text in str(row[0]).lower()]
        #filtered_values = [row for row in all_values if any(search_text in cell.lower() for cell in row)]
            # Update the table with filtered data
        self.mulakat.tableWidgetMul.setRowCount(len(filtered_values))
        for i, row in enumerate(filtered_values):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.mulakat.tableWidgetMul.setItem(i, j, item)
    def projeGelen(self):
        credentials = 'wrherecrmproject-af4aa86d1e43.json'
        gc = gspread.service_account(filename=credentials)
        spreadsheet = gc.open('Mulakatlar')
        worksheet = spreadsheet.get_worksheet(0)
        all_values = worksheet.get_all_values()
        # Verileri tabloya ekle
        mentor_rows = [row for row in all_values[1:] if str(row[2]).lower() and row[2] != '']
        # Update the table with filtered data
        self.mulakat.tableWidgetMul.setRowCount(len(mentor_rows))
        self.mulakat.tableWidgetMul.setHorizontalHeaderLabels(all_values[0])
        self.mulakat.tableWidgetMul.setColumnCount(len(all_values[0]))  # to keep the same number of columns
        for i, row in enumerate(mentor_rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.mulakat.tableWidgetMul.setItem(i, j, item)
    def projeGiden(self):
        credentials = 'wrherecrmproject-af4aa86d1e43.json'
        gc = gspread.service_account(filename=credentials)
        spreadsheet = gc.open('Mulakatlar')
        worksheet = spreadsheet.get_worksheet(0)
        all_values = worksheet.get_all_values()
        #search_text = self.mulakat.lineEdit.text().lower()
        # Verileri tabloya ekle
        mentor_rows = [row for row in all_values[1:] if str(row[1]).lower() and row[1] != '']
        # Update the table with filtered data
        self.mulakat.tableWidgetMul.setRowCount(len(mentor_rows))
        self.mulakat.tableWidgetMul.setHorizontalHeaderLabels(all_values[0])
        self.mulakat.tableWidgetMul.setColumnCount(len(all_values[0]))  # to keep the same number of columns
        for i, row in enumerate(mentor_rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.mulakat.tableWidgetMul.setItem(i, j, item)


    # def ProjeGelen(self):
    #     search_text = self.mulakat.lineEdit.text().lower()
    #     credentials = 'wrherecrmproject-af4aa86d1e43.json'
    #     gc = gspread.service_account(filename=credentials)
    #     spreadsheet = gc.open('Mulakatlar')
    #     worksheet = spreadsheet.get_worksheet(0)
    #     all_values = worksheet.get_all_values()

    # # Sadece dolu satırları filtrele
    #     filtered_values = [row for row in all_values if search_text in str(row[2]).lower()]

    #     if filtered_values != '':
    #     # Set the column count and header labels based on the first row of filtered values
    #         self.mulakat.tableWidgetMul.setColumnCount(len(filtered_values[0]))
    #         self.mulakat.tableWidgetMul.setHorizontalHeaderLabels(filtered_values[0])

    #     # Set the row count and populate the table with filtered values
    #         self.mulakat.tableWidgetMul.setRowCount(len(filtered_values))
    #         for i, row in enumerate(filtered_values):
    #             for j, value in enumerate(row):
    #                 item = QTableWidgetItem(str(value))
    #                 self.mulakat.tableWidgetMul.setItem(i, j, item)

    # def ProjeGiden(self):
    #     search_text = self.mulakat.lineEdit.text().lower()
    #     credentials = 'wrherecrmproject-af4aa86d1e43.json'
    #     gc = gspread.service_account(filename=credentials)
    #     spreadsheet = gc.open('Mulakatlar')
    #     worksheet = spreadsheet.get_worksheet(0)
    #     all_values = worksheet.get_all_values()
    #     # Sadece dolu satırları filtrele

    #     filtered_values = [row for row in all_values if search_text in str(row[1]).lower()]
        
    #     if filtered_values:
    #         self.mulakat.tableWidgetMul.setColumnCount(len(filtered_values[0]))
    #         self.mulakat.tableWidgetMul.setHorizontalHeaderLabels(filtered_values[0])
    #         self.mulakat.tableWidgetMul.setRowCount(len(filtered_values))
    #         for i, row in enumerate(filtered_values):
    #             for j, value in enumerate(row):
    #             #self.mulakat.tableWidgetMul.horizontalHeader().setVisible(False)
    #                 item = QTableWidgetItem(str(value))
    #                 self.mulakat.tableWidgetMul.setItem(i, j, item)



    # def veriyiCekVeTabloyaEkle(self):
    #     # Google Sheets API'ye erişim için gerekli bilgiler
    #     scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    #     creds = ServiceAccountCredentials.from_json_keyfile_name(r'C:\Users\a\Desktop\pyton\crm\credentialse.json', scope)
    #     client = gspread.authorize(creds)

    #     # Google Sheets dokümanının adını veya ID'sini girin
    #     spreadsheet_id = '1c0rP_XlM3RoK9Hpd5sIkUuwvCyKbmgW6KA57y0LtNYo'
    #     sheet_name = 'mulakatkar'

    #     # Belirtilen Google Sheets sayfasındaki verileri çek
    #     sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
    #     veriler = sheet.get_all_values()
        
    #     # QTableWidget içine ekleme
    #     self.mulakat.tableWidgetMul.setRowCount(len(veriler))
    #     self.mulakat.tableWidgetMul.setColumnCount(len(veriler[0]))

    #     for i, row in enumerate(veriler):
    #         for j, value in enumerate(row):
    #             item = QTableWidgetItem(value)
    #             self.mulakat.tableWidgetMul.setItem(i, j, item)

    # def loaddata(self):
    #     connection= {"installed":
    #     {"client_id":"896700188153-idf2o7ba4dablpdadbrkj0eqi8qjid9s.apps.googleusercontent.com",
    #     "project_id":"wrherecrmproject",
    #     "auth_uri":"https://accounts.google.com/o/oauth2/auth",
    #     "token_uri":"https://oauth2.googleapis.com/token",
    #     "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
    #     "client_secret":"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",
    #     "redirect_uris":["http://localhost"]
    #     }}
    #     self.mulakat.tableWidgetMul.setRowCount(0)

    #     for row_number, row_data in enumerate(connection):
    #         self.mulakat.tableWidgetMul.insertRow(row_number)
    #         for colum_number,data in enumerate(row_data):
    #             self.mulakat.tableWidgetMul.setItem(row_number,colum_number,QTableWidgetItem(str(data)))
    #     connection.close()
