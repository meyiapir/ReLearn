from libs.scorer import score
from libs.io import CSVIO, XLSXIO

comments = CSVIO.read('blank.csv')
# comments = XLSXIO.read('blank.xlsx')
comments = list(filter(lambda x: ('' not in x) or (x[3].strip() != ''), comments[:80]))
score = score(comments)

csv_data = []

for item in score.items():
    csv_data.append(item)

CSVIO.write('res.csv', csv_data)
