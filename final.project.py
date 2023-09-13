print('hi!welcome to the world store')

print('we need your information to see the products')

name=input('enter your name')


product_for_female=['makeup','skincare','clothes']
product_for_male=['skincare','clothes','cars']
product_for_kid=['toys','clothes','skincare']
print('are you male ?/ female ?/ kid?')
gender=input('enter your gander')

def funcation_name(gender):

 if gender == ('female'):
    return (product_for_female)

 elif gender == ('male'):
    return(product_for_male)

 elif gender ==  ('kid'):
    return(product_for_kid)
 
print(funcation_name(gender))

makeup_brand=['sephora','MAC','makeup forever']
 
skincare_brand=['cearaVe','Olay','cetaphill']

clothes_brand=['Versace','Zara','Nike']


 
choos1=input('choose one otion makeup / skincare /clothes')
if choos1 == ('mkeupe'):
    print (makeup_brand)

elif choos1 == ('skincare'):
    print (skincare_brand)

elif choos1 ==('clothes'):
    print (clothes_brand)

 
skincare_brand=['cearaVe','Olay','cetaphill']

clothes_brand=['Versace','Zara','Nike']

cars_brand=['BMW','Mercedes-benz','Toyota']

choos2=input('choose one otion skincare /clothes / cars')

if choos2 == ('skincare'):
    print(skincare_brand)

elif choos2 == ('clothes'):
    print (clothes_brand)

elif choos2 == ('cars'):
    print (cars_brand)

toys_brand=['Lego','toysrus','dabaoob']

skincare_brand2=['Johansons baby', 'QV','seba med']
oys_product=['lego harry potter','bingo game','dabaoob']

choos3=input('choose one otion''toys'/'skincare'/'clothes')

if choos3 ==('Lego'):
    print (toys_brand)

elif choos3== ('skincare'):
    print (skincare_brand2)

elif choos3 == ('clothesc'):
    print(clothes_brand)
    


sephora_product=['rose gold','MAC Lipstick','foundation 118']
skincare_product=['motisturising lotion','olay natural white with day dream']

country=['Kuwait','Saudi Arabia','Oman','Qatar','Bahrain','U.A.U']

country=input('entr your country')