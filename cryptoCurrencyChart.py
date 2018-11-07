import pandas as pd
from matplotlib import pyplot as plt

website = 'https://coinmarketcap.com/currencies/bitcoin/historical-data/'
data = pd.read_html(website)
##print(data)

data['Data']
##plt.plot(Date,Open)
