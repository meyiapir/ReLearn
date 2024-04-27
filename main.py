from libs.scorer import score
from libs.csv_io import CSVIO

comments = list(map(lambda x: x[3], CSVIO.read('blank.csv')))
comments = list(filter(lambda x: x.strip() != '', comments))

score = score(comments)

csv_data = []

for item in score.items():
    csv_data.append(item)

CSVIO.write('res.csv', csv_data)
