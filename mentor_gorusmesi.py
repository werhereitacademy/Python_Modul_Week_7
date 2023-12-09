from PyQt6.QtWidgets import *
from mentor import Ui_mentorSayfasi
import gspread


class mentor_sayfasi(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.mentor=Ui_mentorSayfasi()
        self.mentor.setupUi(self)
        ##################################################################################
        self.mentor.TercihlerEkraniButtonMen.clicked.connect(self.tercihler_sayfasina_git)
        self.mentor.tumGorusmelerButton.clicked.connect(self.tabloya_ekle)
        self.mentor.araButtonMen.clicked.connect(self.kisi_ara)
        self.mentor.pushButton_sorgula.clicked.connect(self.combo_box_git)
     #    self.mentor.comboBox.currentTextChanged.connect(self.combo_box_git)
     #    self.mentor.comboBox.setEnabled(True)
        ##################################################################################
    def tercihler_sayfasina_git(self):
        from tercihler_sayfasi import tercih_sayfasi
        self.close()
        self.tercih=tercih_sayfasi()
        self.tercih.show()

        ##################################################################################
    def tabloya_ekle(self):
        credentials = 'wrherecrmproject-af4aa86d1e43.json'
        gc = gspread.service_account(filename=credentials)
        spreadsheet = gc.open('Mentor')
        worksheet = spreadsheet.get_worksheet(0)
        all_values = worksheet.get_all_values()

        # Verileri tabloya ekle
        self.mentor.tableWidgetMen.setColumnCount(len(all_values[0]))
        self.mentor.tableWidgetMen.setHorizontalHeaderLabels(all_values[0])
        self.mentor.tableWidgetMen.setRowCount(len(all_values)-1)

        for i, row in enumerate(all_values[1:]):
                for j, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    self.mentor.tableWidgetMen.setItem(i, j, item)
        #############################################################################
    
    def kisi_ara(self):
         aranan_kisi=self.mentor.lineEditMen.text().lower()
         all_values=self.get_spreadsheet_data()
       
         

         #Verileri ekle
         self.mentor.tableWidgetMen.setColumnCount(len(all_values[0]))
         self.mentor.tableWidgetMen.setHorizontalHeaderLabels(all_values[0])
         self.mentor.tableWidgetMen.setRowCount(0)
        #  person_found=False

         for i, row in enumerate(all_values[1:]): #basligi gec
              if aranan_kisi in str(row).lower():
                   self.mentor.tableWidgetMen.insertRow(self.mentor.tableWidgetMen.rowCount())
                   for j, value in enumerate(row):
                        item=QTableWidgetItem(str(value))
                        self.mentor.tableWidgetMen.setItem(self.mentor.tableWidgetMen.rowCount() -1, j, item)
    

    def combo_box_git(self):
        credentials = 'wrherecrmproject-af4aa86d1e43.json'
        gc = gspread.service_account(filename=credentials)
        spreadsheet = gc.open('Mentor')
        worksheet = spreadsheet.get_worksheet(0)
        all_values =worksheet.get_all_values()

        #Verileri tabloya ekle
        kind = self.mentor.comboBox.currentText()

        if kind == 'VIT projesinin tamamına katılması uygun olur':
             filtered_values=[row for row in all_values if kind.upper() in str(row[4]).upper()]
             for i, row in enumerate(filtered_values[1:]):
                  for j, value in enumerate(row):
                       self.mentor.tableWidgetMen.setColumnCount(len(filtered_values[0]))
                    #    self.mentor.tableWidgetMen.setHorizontalHeaderLabels(filtered_values[0])
                       self.mentor.tableWidgetMen.setRowCount(len(filtered_values))

                       item=QTableWidgetItem(str(value))
                       self.mentor.tableWidgetMen.setItem(i,j,item)
        elif kind == "VIT projesi ilk IT eğitimi alıp ITPH a yönlendirilmesi uygun olur":
             filtered_values=[row for row in all_values if kind.upper() in str(row[4]).upper()]
             for i, row in enumerate(filtered_values):
                  for j, value in enumerate(row):
                       self.mentor.tableWidgetMen.setColumnCount(len(filtered_values[0]))
                    #    self.mentor.tableWidgetMen.setHorizontalHeaderLabels(filtered_values[0])
                       self.mentor.tableWidgetMen.setRowCount(len(filtered_values))

                       item=QTableWidgetItem(str(value))
                       self.mentor.tableWidgetMen.setItem(i,j,item)
        elif kind == "VIT projesi ingilizce eğitimi alıp ITPH a yönlendirilmesi uygun olur":
             filtered_values=[row for row in all_values if kind.upper() in str(row[4]).upper()]
             for i, row in enumerate(filtered_values):
                  for j, value in enumerate(row):
                       self.mentor.tableWidgetMen.setColumnCount(len(filtered_values[0]))
                    #    self.mentor.tableWidgetMen.setHorizontalHeaderLabels(filtered_values[0])
                       self.mentor.tableWidgetMen.setRowCount(len(filtered_values))

                       item=QTableWidgetItem(str(value))
                       self.mentor.tableWidgetMen.setItem(i,j,item)
        elif kind == "VIT projesi kapsamında direkt ITPH a yönlendirilmesi uygun olur.":
             filtered_values=[row for row in all_values if kind.upper() in str(row[4]).upper()]
             for i, row in enumerate(filtered_values):
                  for j, value in enumerate(row):
                       self.mentor.tableWidgetMen.setColumnCount(len(filtered_values[0]))
                    #    self.mentor.tableWidgetMen.setHorizontalHeaderLabels(filtered_values[0])
                       self.mentor.tableWidgetMen.setRowCount(len(filtered_values))

                       item=QTableWidgetItem(str(value))
                       self.mentor.tableWidgetMen.setItem(i,j,item)
        elif kind == "Direkt bireysel koçluk ile işe yönlendirilmesi uygun olur":
             filtered_values=[row for row in all_values if kind.upper() in str(row[4]).upper()]
             for i, row in enumerate(filtered_values):
                  for j, value in enumerate(row):
                       self.mentor.tableWidgetMen.setColumnCount(len(filtered_values[0]))
                    #    self.mentor.tableWidgetMen.setHorizontalHeaderLabels(filtered_values[0])
                       self.mentor.tableWidgetMen.setRowCount(len(filtered_values))

                       item=QTableWidgetItem(str(value))
                       self.mentor.tableWidgetMen.setItem(i,j,item)
        elif kind == "Bir sonraki VIT projesine katilmasi daha uygun olur":
             filtered_values=[row for row in all_values if kind.upper() in str(row[4]).upper()]
             for i, row in enumerate(filtered_values):
                  for j, value in enumerate(row):
                       self.mentor.tableWidgetMen.setColumnCount(len(filtered_values[0]))
                    #    self.mentor.tableWidgetMen.setHorizontalHeaderLabels(filtered_values[0])
                       self.mentor.tableWidgetMen.setRowCount(len(filtered_values))

                       item=QTableWidgetItem(str(value))
                       self.mentor.tableWidgetMen.setItem(i,j,item)
        elif kind == "Başka bir sektöre yönlendirilmeli":
             filtered_values=[row for row in all_values if kind.upper() in str(row[4]).upper()]
             for i, row in enumerate(filtered_values):
                  for j, value in enumerate(row):
                       self.mentor.tableWidgetMen.setColumnCount(len(filtered_values[0]))
                    #    self.mentor.tableWidgetMen.setHorizontalHeaderLabels(filtered_values[0])
                       self.mentor.tableWidgetMen.setRowCount(len(filtered_values))

                       item=QTableWidgetItem(str(value))
                       self.mentor.tableWidgetMen.setItem(i,j,item)
        elif kind == "Diger":
             filtered_values=[row for row in all_values if kind.upper() in str(row[4]).upper()]
             for i, row in enumerate(filtered_values):
                  for j, value in enumerate(row):
                       self.mentor.tableWidgetMen.setColumnCount(len(filtered_values[0]))
                    #    self.mentor.tableWidgetMen.setHorizontalHeaderLabels(filtered_values[0])
                       self.mentor.tableWidgetMen.setRowCount(len(filtered_values))

                       item=QTableWidgetItem(str(value))
                       self.mentor.tableWidgetMen.setItem(i,j,item) 
     




    def get_spreadsheet_data(self):
         credentials = 'wrherecrmproject-af4aa86d1e43.json'
         gc = gspread.service_account(filename=credentials)
         spreadsheet = gc.open('Mentor')
         worksheet = spreadsheet.get_worksheet(0)
         return worksheet.get_all_values()

