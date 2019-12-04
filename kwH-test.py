"""Kruskal-Wallis H Test"""

import numpy as np
import pandas as pd 
from sys import argv
from scipy.stats import chi2


def get_data(fn):
	df = pd.read_csv(fn, header=None)
	df.columns = ['wom', 'men', 'min']
	return df

def extract_list_from_df(df):
	df = df.T
	return df.values.tolist()

def calc_H(data, ranks, sample_sizes):
	n = float(len(data))
	T_2 = lambda col: (pow(ranks[col], 2.), col)
	E = lambda tup: tup[0] / sample_sizes[tup[1]]

	Ts = list(map(T_2, list(ranks)))
	Es = list(map(E, Ts))

	a = 12. / (n*(n+1.))
	b = sum(Es)
	c = 3. * (n+1.)

	return a * b - c

def sort_data(tuples):
	return sorted(tuples, key=lambda x: x[0])

def get_tuples(df):
	tuples = list()
	for col in list(df):
		col_list = [col for _ in range(len(df[col]))]
		tuples  += zip(df[col], col_list)
	return tuples

def get_sampl_sizes(df):
	sample_sizes = {}
	for cat in list(df):
		sample_sizes[cat] = len(df[cat])
	return sample_sizes

def get_ranks(tuples, categories):
	ranks = {}
	for category in categories:
		ranks[category] = 0
	for i, tup in enumerate(tuples):
		ranks[tup[1]] += i+1
	return ranks

def calc_critical_score(alpha, dof):
	return chi2.isf(alpha, dof)

def comp_tests(H, cv):
	print(H-cv)
	if H > cv: 
		print('**Medians unequal, reject null hypothesis!**')
		return
	print('Medians equal, accept null hypothesis')


def main():
	"""P-value for this example data is p=0.0347
	P-value with bonferroni correction = alpha / no-tests
	e.g. 0.05 / 6 = 0.0083
	"""
	assert len(argv) > 2, 'Usage: hwH-test.py [datafile.csv] [alpha]'
	df, alpha = get_data(argv[1]), float(argv[2])
	print('Data:')
	print(df)
	cols = list(df)
	tuples = get_tuples(df)
	sorted_data = sort_data(tuples)
	sample_sizes = get_sampl_sizes(df)
	ranks = get_ranks(sorted_data, cols)
	print('Ranks:', ranks)
	H = calc_H(sorted_data, ranks, sample_sizes)
	print('H statistic:', H)
	crit_val = calc_critical_score(alpha, 2)
	print('Critical Chi-Squared value:', crit_val)
	comp_tests(H, crit_val)



if __name__ == "__main__":
	main()