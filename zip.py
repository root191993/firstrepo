from typing import Dict

names = ('Pavan','Rohini','Sree','Yugu','Pavan')
comps = ('TCS', 'Orchids','Gainwell','Siemns','Wipro')

zipped = zip(names,comps)

for (a,b) in zipped:
    print(a,b)

