import sys

from PyQt5 import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from model import *
from model.offlineAPI import OfflineAPI
from model.onlineAPI import OnlineAPI

from view import view


class Controller(QMainWindow):
    """
    Controller Klasse die Model und View verknüpft
    """

    def __init__(self):
        super().__init__()
        self.ui = view.Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.umrechnenButton.clicked.connect(self.umrechnen)
        self.ui.exitButton.clicked.connect(self.exit)
        self.ui.resetButton.clicked.connect(self.reset)
        self.ui.liveDatenBox.clicked.connect(self.live)
        self.strat = OfflineAPI()
        # self.title = "Währungsumrechner"
        # self.initUI()

    def live(self, checked):
        """
        Überprüft ob live Daten oder offline Daten verwendet werden sollen
        :param checked: true wenn live Daten verwendet werden sollen
        :return: Wenn true, dann wird ein Online Objekt erstellt. wenn false wird ein Offline Objekt erstellt
        """

        if checked:
            self.strat = OnlineAPI()
        else:
            self.strat = OfflineAPI()

    def umrechnen(self):
        """
        Das ist die Umrechnen Methode

        :return: der neue Wert
        """

        self.setHTML(
            self.strat.change(self.ui.betragInput.value(), self.ui.waehrungInput.text(), self.ui.zielInput.text()))

        self.ui.statusLabel.setText("OK")

    def exit(self):
        """
        Eine Alternative um das Fenster zu schließen und das Programm zu beenden

        :return: Die Application wird geschlossen
        """

        QtCore.QCoreApplication.instance().quit()

    def reset(self):
        """
         Löscht alle Felder

        :return: alle Felder werden gecleared
        """

        self.ui.waehrungInput.setText("")
        self.ui.zielInput.setText("")
        self.ui.betragInput.setValue(0.00)
        self.ui.textBrowser.setText("")
        self.ui.statusLabel.setText("Status:")

    def setHTML(self, text):
        """
        Setzt den Text der durch die Berechnung generiert wird in das HTML Fenster

        :param text: der HTML Code der gesetzt wird
        :return: HTML Text im Fenster
        """

        self.ui.textBrowser.append(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = Controller()
    c.show()
    # c.refresh()
    sys.exit(app.exec_())
