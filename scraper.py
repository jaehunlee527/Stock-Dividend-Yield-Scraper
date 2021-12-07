import pandas as pd
from bs4 import BeautifulSoup
import urllib
import urllib.request as ur
import requests
from lxml import html

# Get 1 year dividend & current market cap
def fetch_div(symbol, div_dict, cap_dict, ind_dict): 
	# Check repeated symbol
    if symbol in div_dict:
        return
    
    # Fetch url by ticker symbol
    try:
    	url_is = "https://finance.yahoo.com/quote/"+ symbol + "?p=" + symbol
    	url_mk = "https://www.marketwatch.com/investing/stock/" + symbol.lower() + "/company-profile?mod=mw_quote_tab"
    	headers = {"User-Agent":"Mozilla/5.0"}
    	response = requests.get(url_is, headers=headers, timeout=5)
    	parser = html.fromstring(response.text)
    	soup = BeautifulSoup(response.text, 'lxml')

    except Exception as e:
        print(e," Ticker Not Found")
        return
    
    # Fetch Dividend Yield %
    try:
        xpath_div = "//td [@data-test='DIVIDEND_AND_YIELD-value']/text()"
        div = parser.xpath(xpath_div)
        div = div[0]
        div_dict[symbol] = div.split(" ")[1]
    except:
        div_dict[symbol] = "N/A"
        print("Error: Dividend Yield Not Found")
    
    # Fetch Market Cap
    try:
        xpath_cap = "//td [@data-test='MARKET_CAP-value']/text()"
        cap = parser.xpath(xpath_cap)
        cap = cap[0]
        cap_dict[symbol] = cap
    except:
        cap_dict[symbol] = "N/A"
        print("Error: Market Cap Not Found")
    
    # Fetch industry type
    try: 
        response = requests.get(url_mk,headers=headers, timeout=5)
        parser = html.fromstring(response.text)
        soup = BeautifulSoup(response.text, 'lxml')
        ind_dict[symbol] = soup.find("div", class_="group left").find("span", class_="primary").text
    except:
        ind_dict[symbol] = "N/A"
        print("Error: Industry Type Not Found")
    
    print(symbol, "Loading Complete")
    
    return div_dict, cap_dict, ind_dict