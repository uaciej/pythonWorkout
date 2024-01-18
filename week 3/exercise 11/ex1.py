'''
Sort a list of dicts first by lastname then by firstname and return the list of sorted dicts
'''

PEOPLE = [{'first':'Reuven', 'last':'Lerner',
'email':'reuven@lerner.co.il'},
{'first':'Donald', 'last':'Trump', 'email':'president@whitehouse.gov'},
{'first':'Vladimir', 'last':'Putin',
'email':'president@kremvax.ru'}
]

def dic_sorter(lis):
    return sorted(lis, key=lambda x: [x['last'], x['first']])

for person in dic_sorter(PEOPLE):
    print(person)