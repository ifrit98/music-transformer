import pandas as pd 
import numpy as np 
from sys import argv

SCORES = {'Beethoven': [], 'Chopin': [], 'Debussy': [], 
				'Jarrett': [], 'Tatum': []}

PAIRS = {0: ['Beethoven', 'Chopin'],  1: ['Debussy', 'Beethoven'],
		 2: ['Beethoven', 'Jarrett'], 3: ['Tatum', 'Beethoven'],
		 4: ['Chopin', 'Debussy'],    5: ['Jarrett', 'Chopin'],
		 6: ['Chopin', 'Tatum'],      7: ['Debussy', 'Jarrett'],
		 8: ['Tatum', 'Debussy'],     9: ['Jarrett', 'Tatum']}

fn = argv[1] if len(argv) > 1 else ''

with open(fn, 'rb') as f:
	lines = list(f.readlines())
	contents = []
	lines = lines[1:]

	for line in lines:
		temp = line.split(',')
		content = []

		for i in range(len(temp)):
			if 'first' in temp[i].lower():
				if 'definitely' in temp[i+1].lower():
					content.append(1.)
				elif 'somewhat' in temp[i+1].lower():
					content.append(2.)
			elif 'second' in temp[i].lower():
				if 'definitely' in temp[i+1].lower():
					content.append(5.)
				elif 'somewhat' in temp[i+1].lower():
					content.append(4.)
			elif 'neutral' in temp[i].lower():
				content.append(2.5)

		contents.append(content)

df = pd.DataFrame.from_records(contents)
print(df)

for idx, row in df.iterrows():
	print('Row:',row)
	for i in range(len(row)):
		pair = PAIRS[i]
		if row[i] == 5.:
			SCORES[pair[0]].append(1.)
			SCORES[pair[1]].append(5.)
		elif row[i] == 4.:
			SCORES[pair[0]].append(2.)
			SCORES[pair[1]].append(4.)
		elif row[i] == 2.:
			SCORES[pair[0]].append(4.)
			SCORES[pair[1]].append(2.)
		elif row[i] == 1.:
			SCORES[pair[0]].append(5.)
			SCORES[pair[1]].append(1.)
		else:
			SCORES[pair[0]].append(2.5)
			SCORES[pair[1]].append(2.5)

for k,v in SCORES.items():
	print(k,np.mean(v))