print('KUSOO DHAWOOW ALALE ROBOT    ')


print ('fadlan si aan kuugu sheego jawaabta saxda ah fadlan sisaxa u raac talaaba walba oo aan kuu sheego: ')

divide = input ('fadlan kala saar raga iyo dumarka: taabo Enter hadii aad kala saartay: ')

libin = input('fadlan libin laab tirada raga: taabo Enter hadii aad libin laabtay: ')

ugayn = input('fadlan ugee sadex tiradii aad libin laabtay ee Raga: taabo Enter hadii ad ugaysay:  ')

kudhufo = input ('fadlan shan ku dhufo tirada aad hayso hada ee Raga:taabo Enter hadii ku dhufatay: ')

final = input('fadlan ugee tirada dumarka hadii ay jiraan totalka tirada aad hayso: ')

ok = int (input('fadlan gali iskugaynta guud ee tirada si aan kuugu sheego inta dumara iyo inta raga: '))





lk = ok - 15


ani = [lk]

make = ani

digits = [str(x) for x in str(make)]
# print(digits)




d = (digits[2])

if ok >=100:
    second = (digits[1] + digits[2])
    third = (digits[3])
    print(second + ' ' + ' rag ah')
    print(third + ' ' + ' dumara')


elif ok < 25 :
    print(digits[1] + ' ' + 'gabadh ayay dhaleen ')
    print('wax rag ah may dhalin')
elif ok >= 25:
    print(digits[1] + ' ' + 'Rag ah')
    print(digits[2] + ' ' + 'dumara')

if d == '0':
    
    print('wax dumara may dhalin')
    


    






# print(str( lk))
