# Simulated SmartApi/smartConnect.py
class SmartConnect:
    def __init__(self, api_key=None):
        self.api_key = api_key

    def generateSession(self, client_id, password, totp):
        return {"status": "success", "client_id": client_id}

    def getInstruments(self, exchange):
        return [{"name": "NIFTY", "expiry": "2025-09-25", "strike": 20000, "optiontype": "CE",
                 "tradingsymbol": "NIFTY25SEP20000CE", "token": "12345", "lotsize": 75}]

    def getCandleData(self, params):
        # Return dummy data for demonstration
        return [[
            "2025-09-02 09:15", 20000, 20050, 19950, 20010, 100000
        ]]

    def ltpData(self, exchange, tradingsymbol, token):
        return {"data": {"ltp": 20010}}

    def placeOrder(self, **kwargs):
        return {"orderid": "ORDER12345"}
