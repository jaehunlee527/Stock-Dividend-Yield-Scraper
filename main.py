from scraper import *
from df_caller import *

def main():
	# List of Stock Symbol
	index= ["NYMT","LADR","NRZ","PLYM","MNR","ILPT","EGP","STAG","FR","REXR","UMH","NXRT",
	       "IRT","CLPR","BRG","APTS","INVH","AMH","MAA","CPT","ACC","SUI","UDR","CONE","QTS","COR","EQIX","DLR",
	       "AMT","CCI","PLD","SPG","WELL","EQR","AVB","AGNC","ABR","ARR","BXMT","STWD","STAR","CLNC","TRTX","CMO",
	        "KREF","AGNC","NLY"]

	tmp = ["LADR","NRZ"]

	div_dict = {}
	cap_dict = {}
	ind_dict = {}

	for symbol in tmp:
	    fetch_div(symbol, div_dict, cap_dict, ind_dict)

	df = df_caller(div_dict, cap_dict, ind_dict) 
	print("\n", df)
	
	return df 

if __name__ == '__main__':
    main()