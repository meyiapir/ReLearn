from libs.csv_io import CSVIO
from libs.scorer import score

csv = CSVIO.read('scored.csv')[:80]

stat = [0, 0, 0, 0]

for line in csv:
    if line[3] != "":
        scored = line[-4:]
        print(line)
        res = score([line])
        print(res)
        predicted = (res['positive'], res['swear'], res['tech'], res['complexity'])

        for i in range(4):
            if abs(float(scored[i]) - float(predicted[i])) <= 0.2:
                stat[i] += 1


stat = list(map(lambda x: x/len(csv)))

print('pos swear tech complex')

for s in stat:
    print(s*100, '%')