import sys, getopt
import csv
import json

csv_rows = []
with open('10yearAUSOpenMatches.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    title = reader.fieldnames
    for row in reader:
        csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])

print(csv_rows[0]['player1'])
print(csv_rows[0]['player2'])

#csv_rows2 = { 'name': csv_rows[0]['player1']  }
#/csv_rows3 = { 'name': csv_rows[0]['player2']  }
#csv_rows4 = { 'name': csv_rows[0]['player1'] , 'children': [csv_rows2 , csv_rows3]}
count = 0

idlist = []
linklist = []
finaldict = {"nodes": [], "links": []}
count = 0
"""""
for row in csv_rows:
   count = count + 1
   if row['year'] == '2009' and row['round'] == 'Final':
       winner = row['player1']
       dict1 = {'id': winner }
       dict4 = {"source": winner, "target": row['player2']}
       linklist.append(dict4)
       idlist.append(dict1)

   if row['player1'] == winner and row['round'] != 'Final':
       dict2 = {'id': row['player2'] }
       idlist.append(dict2)
       dict3 = {"source": winner, "target": row['player2']}
       linklist.append(dict3)

"""
year = '2009'
list1 = []
# first get list of all unique players in a year (both player 1 and 2)
for row in csv_rows:
    if row['year'] == year and (row['round'] != 'First' and row['round'] != 'Second' and row['round'] != 'Third'
                                ):
        list1.append(row['player1'])
        list1.append(row['player2'])

list2 = list(set(list1))

print(list2)

dictk = dict.fromkeys(list2)
count = 0
dict1 = []
for l in list2:
    dictk[l] = count
    count = count + 1
    for r in csv_rows:
        if r['round'] == 'Final' and r['player1'] == l and r['year'] == year:
            dict1 = {'id': l, 'winner': 'yes' }
            break
        else:
            dict1 = {'id': l, 'winner': 'no' }
    idlist.append(dict1)
print(dictk)
print(idlist)

for row in csv_rows:
  if row['year'] == year and (row['round'] != 'First' and row['round'] != 'Second' and row['round'] != 'Third' ):
    dict3 = {"source": dictk[row['player1']], "target": dictk[row['player2']], "result": row['results']}
    linklist.append(dict3)

#idlist_unique = [dict(t) for t in{tuple(d.items())for d in idlist}]
#print(idlist_unique)
finaldict = {"nodes": idlist, "links": linklist}




print(finaldict)

with open('data_all.json', 'w') as f:
    f.write(json.dumps(finaldict, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False))
