from multiprocessing.sharedctypes import Value

print(' ')
print(' ')
print(' ')
print('zmiana na lepsze ')
print(' ')

sklep  = {
    'Biedronka' : ['chleb','bulka','ciasto','cebula'],
    'Zabka' : ['paluszki','hot-dog',]

}

for keys ,value  in sklep.items():

    print(f'Ide do sklepu',keys,'i kupuje ',value ,' kupuję ',len(value), 'produkty',)
    
