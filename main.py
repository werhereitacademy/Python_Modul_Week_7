from PyQt6.QtWidgets import QApplication
from giris_sayfasi import girissayfasi
app=QApplication([])
pencere=girissayfasi()
pencere.show()
app.exec()