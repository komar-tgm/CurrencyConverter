from model import AbstractAPI


class OfflineAPI(AbstractAPI.ConverterService):
    """
    Offline Klasse die die Berechnung mittels vordefinierten Kursen durchführt
    """

    def __init__(self):
        pass

    def change(self, ammount, curFrom, curTo):
        """
            Methode die Währungen umrechnet und als schönen HTML Text zurückgibt
            :param ammount: Geldmenge
            :param curFrom: Ursprungswährung
            :param curTo: Endwähtungen
            :return: fertiger HTML Code für das Fenster
        """
        curList = curTo.split(',')
        date = '2019-10-13'
        api = {
            'CAD': 1.4679,
            'HKD': 8.6614,
            'ISK': 137.7,
            'PHP': 56.927,
            'DKK': 7.4688,
            'HUF': 331.71,
            'CZK': 25.807,
            'AUD': 1.6246,
            'RON': 4.7573,
            'SEK': 10.8448,
            'IDR': 15601.55,
            'INR': 78.4875,
            'BRL': 4.5291,
            'RUB': 70.8034,
            'HRK': 7.428,
            'JPY': 119.75,
            'THB': 33.642,
            'CHF': 1.1025,
            'SGD': 1.5177,
            'PLN': 4.3057,
            'BGN': 1.9558,
            'TRY': 6.4713,
            'CNY': 7.8417,
            'NOK': 10.0375,
            'NZD': 1.7419,
            'ZAR': 16.3978,
            'USD': 1.1043,
            'MXN': 21.3965,
            'ILS': 3.8673,
            'GBP': 0.87518,
            'KRW': 1308.61,
            'MYR': 4.622,
            'EUR': 1.0
        }
        print(api)
        print(curFrom)

        ammountInEur = ammount / api[curFrom]
        print(ammountInEur)

        multis = []
        changedVal = []
        for cur in curList:
            changedVal.append(ammountInEur * api[cur])
            multis.append(api[cur])

        print(changedVal)

        htmlOutput = '<p><b>' + str(ammount) + ' ' + curFrom + '</b> entsprechen</p><ul>'

        for i in range(len(changedVal)):
            htmlOutput += '<li><b>' + str(changedVal[i]) + ' ' + curList[i] + '</b> (Kurs:' + str(multis[i]) + ')</li>'

        htmlOutput += '</ul><p>Stand: ' + date
        return htmlOutput
