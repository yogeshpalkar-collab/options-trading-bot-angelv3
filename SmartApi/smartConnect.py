import random, datetime

class SmartConnect:
    def __init__(self, api_key=None):
        self.api_key = api_key

    def generateSession(self, client_id, password, totp):
        return {"status": "success", "client_id": client_id}

    def getInstruments(self, exchange):
        # Simulated: return all Tuesdays + monthly expiry for NIFTY
        return [
            {"name": "NIFTY", "expiry": "2025-09-02", "strike": 20000, "optiontype": "CE",
             "tradingsymbol": "NIFTY25SEP20000CE", "token": "12345", "lotsize": 75},
            {"name": "NIFTY", "expiry": "2025-09-09", "strike": 20000, "optiontype": "CE",
             "tradingsymbol": "NIFTY25SEP20000CE", "token": "12346", "lotsize": 75},
            {"name": "NIFTY", "expiry": "2025-09-16", "strike": 20000, "optiontype": "CE",
             "tradingsymbol": "NIFTY25SEP20000CE", "token": "12347", "lotsize": 75},
            {"name": "NIFTY", "expiry": "2025-09-23", "strike": 20000, "optiontype": "CE",
             "tradingsymbol": "NIFTY25SEP20000CE", "token": "12348", "lotsize": 75},
            {"name": "NIFTY", "expiry": "2025-09-25", "strike": 20000, "optiontype": "CE",
             "tradingsymbol": "NIFTY25SEP20000CE", "token": "12349", "lotsize": 75},
        ]

    def getCandleData(self, params):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        return [[now, 20000, 20050, 19950, 20010, 100000]]

    def ltpData(self, exchange, tradingsymbol, token):
        return {"data": {"ltp": 20000 + random.randint(-20, 20)}}

    def placeOrder(self, **kwargs):
        return {"orderid": f"ORDER-{random.randint(1000,9999)}"}
