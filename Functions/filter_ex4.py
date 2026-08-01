# keep only words layer then 3 characters.
words = ['hi','hello','sun']
print(list(filter(lambda s: len(s)>=3,words)))

#keep only positive numbers from a mixed list numbers 
numbers= [-3,2,11,20]
print(list(filter(lambda s: s>0,numbers)))