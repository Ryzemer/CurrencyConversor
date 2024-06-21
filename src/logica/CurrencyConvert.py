import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class Dialogo(QMainWindow):
    # Tipo de cambio al 20240619
    USDtoPEN = 3.84
    USDtoEUR = 0.93
    USDtoGBP = 0.79  # Tasa de cambio USD a GBP
    GBPtoPEN = 4.81  # Tasa de cambio GBP a PEN

    def __init__(self):
        super().__init__()
        ruta = os.path.dirname(os.path.abspath(__file__)) + r"\..\vista\currencyConvert.ui"
        uic.loadUi(ruta, self)

        self.pbTipoCambio.clicked.connect(self.calcularConversion)

    def calcularConversion(self):
        convertido = 0.0
        inicial = 0.0

        try:
            inicial = float(self.leImporte.text())

            if self.rbDeUSD.isChecked():
                if self.rbAEUR.isChecked():
                    convertido = inicial * self.USDtoEUR
                elif self.rbAPEN.isChecked():
                    convertido = inicial * self.USDtoPEN
                elif self.rbAGBP.isChecked():
                    convertido = inicial * self.USDtoGBP

            elif self.rbDeEUR.isChecked():
                if self.rbAUSD.isChecked():
                    convertido = inicial / self.USDtoEUR
                elif self.rbAPEN.isChecked():
                    convertido = inicial * (self.USDtoPEN / self.USDtoEUR)
                elif self.rbAGBP.isChecked():
                    convertido = inicial * (self.USDtoGBP / self.USDtoEUR)

            elif self.rbDePEN.isChecked():
                if self.rbAUSD.isChecked():
                    convertido = inicial / self.USDtoPEN
                elif self.rbAEUR.isChecked():
                    convertido = inicial * (self.USDtoEUR / self.USDtoPEN)
                elif self.rbAGBP.isChecked():
                    convertido = inicial * (self.GBPtoPEN / self.USDtoPEN)

            elif self.rbDeGBP.isChecked():
                if self.rbAUSD.isChecked():
                    convertido = inicial / self.USDtoGBP
                elif self.rbAEUR.isChecked():
                    convertido = inicial * (self.USDtoEUR / self.USDtoGBP)
                elif self.rbAPEN.isChecked():
                    convertido = inicial / self.GBPtoPEN

        except ValueError:
            self.lblCambio.setText("Error: Ingrese un número válido.")

        self.lblCambio.setText(f"{convertido:.2f}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = Dialogo()
    dialogo.show()
    sys.exit(app.exec_())
