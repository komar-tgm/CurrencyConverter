import requests
from model import AbstractAPI


class OnlineAPI(AbstractAPI.ConverterService):
    """
        Online Klasse die die Umrechnung mittels REST API durchführt
    """

    def __init__(self):
        self.output = []
        self.url = "https://api.exchangeratesapi.io/latest"

    def change(self, ammount, curFrom, curTo):
        """
        Methode die Währungen umrechnet und als schönen HTML Text zurückgibt
        :param ammount: Geldmenge
        :param curFrom: Ursprungswährung
        :param curTo: Endwähtungen
        :return: fertiger HTML Code für das Fenster
        """
        curList = curTo.split(',')
        multis = []
        print(curList)
        for cur in curList:
            params = {"base": curFrom,
                      "symbols": curTo
                      }
            resp = requests.get(self.url, params=params)
            if resp.status_code != 200:
                raise ValueError(self.output.format(resp.status_code))
            self.output = resp.json()
            print(self.output)
            multis.append(self.output['rates'][cur])

        print(multis)

        date = self.output['date']
        print(date)
        changedVal = []
        for m in multis:
            changedVal.append(ammount * m)

        print(changedVal)

        htmlOutput = '<p><b>' + str(ammount) + ' ' + curFrom + '</b> entsprechen</p><ul>'

        for i in range(len(changedVal)):
            htmlOutput += '<li><b>' + str(changedVal[i]) + ' ' + curList[i] + '</b> (Kurs:' + str(multis[i]) + ')</li>'

        htmlOutput += '</ul><p>Stand: ' + date
        return htmlOutput
