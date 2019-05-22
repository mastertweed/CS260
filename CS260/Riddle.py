name = ['B', 'F', 'H', 'L']
title = ['PM', 'APM', 'EE', 'ME']
years = [10, 14, 17, 21]

combos = []
for n in range(4):
    for t in range(4):
        for y in range(4):
            combos.append([name[n], title[t], years[y]])

slot1Criteria = ['F','B','PM','ME','EE']
slot2Criteria = []
slot3Criteria = []
slot4Criteria = []

for i in range(len(combos)):
    if combos[i][0] == 'H' or combos[i][0] == 'L':


