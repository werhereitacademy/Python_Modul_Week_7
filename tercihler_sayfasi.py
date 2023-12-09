from PyQt6.QtWidgets import *
from tercihlersayfasi import Ui_TercihlerSayfasi
from mentor_gorusmesi import mentor_sayfasi
from basvuru_sayfasi import basvurular_sayfasi
from mulakat_sayfasi import mulakatlar_sayfasi


class tercih_sayfasi(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.tercih=Ui_TercihlerSayfasi()
        self.tercih.setupUi(self)
        self.mentorgorussayfasi=mentor_sayfasi()
        self.tercih.mentorgorusmesiButton.clicked.connect(self.MentorGorusmesi)
        self.basvuru=basvurular_sayfasi()
        self.tercih.basvruButton.clicked.connect(self.BasvuruGit)
        self.mulakat=mulakatlar_sayfasi()
        self.tercih.mulakatButton.clicked.connect(self.MulakatGit)
    def MentorGorusmesi(self):
        self.close()
        self.mentorgorussayfasi.show()
    def BasvuruGit(self):
        self.close()
        self.basvuru.show()
    def MulakatGit(self):
        self.close()
        self.mulakat.show()


