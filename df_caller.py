from scraper import *

def df_caller(div_dict, cap_dict, ind_dict):
	# Create DataFrame
	df_div = pd.DataFrame.from_dict(div_dict, orient = 'index', columns=['Dividend Yield %'])
	df_cap = pd.DataFrame.from_dict(cap_dict, orient = 'index', columns=['Market Cap'])
	df_ind = pd.DataFrame.from_dict(ind_dict, orient = 'index', columns=['Industry Type'])

	df = df_div.merge(df_cap, left_index=True, right_index=True)
	df = df.merge(df_ind, left_index=True, right_index=True)

	return df