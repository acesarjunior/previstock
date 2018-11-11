from pinance import Pinance
import json
from frontend.login import symbol

#symbol='AMD'

stock = Pinance(symbol)
stock.get_quotes()
#Convert to JSON
stockdata=stock.quotes_data
jsonstockdata=json.dumps(stockdata)
resp = json.loads(jsonstockdata)
print(resp)

goldenratio=[0.382,0.618,1.382,1.618]

candlewave1 = 5.00
startwave1 = float(resp["regularMarketPreviousClose"])
endwave1 = float(resp["regularMarketPrice"])
timeperiodwave1=endwave1-startwave1