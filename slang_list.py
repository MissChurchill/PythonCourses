acronyms = []

acronyms.append('LOL')
acronyms.append('IDK')
print(acronyms)

acronyms.append('SMH')
acronyms.append('TBH')
acronyms.append('BFN')

print(acronyms)

acronyms.remove('BFN')

print(acronyms)

del acronyms[3]
print(acronyms)

word = 'BFN'
if word in acronyms:
    print(word + ' is in the list')
else:
    print(word + ' is NOT in the list') 
    
for acronym in acronyms:
    print(acronym)    
       
acronyms = {'LOL': 'laugh out loud',
           'IDK': "I don't know",
           'TBH': 'to be honest'}  

print(acronyms['LOL']) 

#create an empty dictionary
acronyms = { }

#adding new dictionary items:
acronyms['LOL']= 'laugh out loud'
acronyms['IDK']= "I don't know"
acronyms['TBH']= 'to be honest'
print(acronyms)

#if you want to get a word in the dictionary, use get()
definition = acronyms.get('BTW')
print(definition)

if definition:
    print(definition)
else:
    print("key does not exist")
    
sentence = 'IDK' + ' what happended ' + 'TBH'
translation = acronyms.get('IDK') + ' what happened ' + acronyms.get('TBH')
print('sentence:', sentence)
print('translation:', translation)
