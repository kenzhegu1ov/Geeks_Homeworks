GeekTech = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
del GeekTech['bag']
GeekTech['address:'] = 'Ibraimova 103,SC Victory,right wing,4th floor'
GeekTech['Inst:'] = 'geektech_edu'
GeekTech['Phone number:'] = '996507052018'
GeekTech['courses'].append('IOS')
GeekTech['courses'].append('Ux/Ui')
GeekTech['courses'].append('Project Manager')
GeekTech['courses'].append('Basics of programming')
GeekTech['courses'] = set(GeekTech['courses'])
GeekTech['founding date:'] = '2018'
a = str(GeekTech['founding date:'])
for key, value in GeekTech.items():
    print(key, value)
number_of_courses =(len(GeekTech['courses']))
print('Number of courses:', number_of_courses)
