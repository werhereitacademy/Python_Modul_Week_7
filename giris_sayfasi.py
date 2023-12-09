
from PyQt6.QtWidgets import *
from girissayfasi import Ui_GirisSayfasi
from tercihler_sayfasi import tercih_sayfasi
import gspread
class girissayfasi(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.giris=Ui_GirisSayfasi()
        self.giris.setupUi(self)
        self.tercihlersayfasiac=tercih_sayfasi()
        self.giris.girisButton.clicked.connect(self.GirisYap)
        
    def GirisYap(self):
        
        search_text = self.giris.lineEdit_1.text()
        search_text2 = self.giris.lineEdit_2.text()

        if search_text and search_text2:
            credentials = 'wrherecrmproject-af4aa86d1e43.json'
            gc = gspread.service_account(filename=credentials)
            spreadsheet = gc.open('Kullanicilar')
            worksheet = spreadsheet.get_worksheet(0)
            all_values = worksheet.get_all_values()
            matching_row = [row for row in all_values if search_text in str(row[0]) and search_text2 in str(row[1])]

            if matching_row:
                self.close()
                self.tercihlersayfasiac.show()
            else:
                self.giris.labelBilgi.setStyleSheet("color: rgb(255, 0, 0);")
                self.giris.labelBilgi.setText('Kullanıcı adı veya şifre hatalı.')
        else:
            self.giris.labelBilgi.setStyleSheet("color: rgb(255, 0, 0);")
            self.giris.labelBilgi.setText('Kullanıcı adı ve şifre boş bırakılamaz.')