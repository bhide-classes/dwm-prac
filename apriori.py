import itertools
import numpy
import csv
with open("C:/Users/Damayanti/OneDrive/Desktop/New folder/dwm/new/Apriori/data_apriori.csv", 'r') as file:
    dataset = list(csv.reader(file))
    items = data = dataset[0]
    del dataset[0]
file.close()
transactions = [''.join(char for char in trans) for trans in dataset]
min_support = (int(input("Enter the minimun support (in %): ")))/100
thrs_conf = (int(input("Enter the minimun confidence (in %): ")))/100
size = len(transactions)
iteration = 1
store = dict()
database = list()
while True:
    itemset = dict()
    for item in items:
        support = 0
        for trans in transactions:
            if len(set([trans.count(char) for char in item])) == 1:
                support += [trans.count(char) for char in item][0]
        if support/len(transactions) >= min_support:
            itemset[item] = support/len(transactions)
    store.update(itemset)
    data = sorted(list(set(''.join(char for char in list(itemset.keys())))))
    iteration += 1
    items = [''.join(item for item in list(i))
             for i in itertools.combinations(data, iteration)]
    if len(itemset) == 0:
        itemset = database[-1]
        break
    database.append(itemset)
items = [list(item) for item in itemset.keys()]
confidence = dict()
for rule in items:
    for i in range(len(rule)-1):
        for elem in list(list(i) for i in itertools.combinations(rule, i+1)):
            confidence[''.join(char for char in elem)] = ''.join(
                char for char in numpy.setdiff1d(rule, elem))
print("The final rules are : ")
for rule in confidence:
    if (store[''.join(sorted(f'{rule}{confidence[rule]}'))]/store[rule]) >= thrs_conf:
        print(f'{rule} --> {confidence[rule]}')