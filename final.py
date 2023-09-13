makeup_brand=['sephora','MAC','makeup forever']
 
skincare_brand=['cearaVe','Olay','cetaphill']

clothes_brand=['Gucci','Zara','Nike']


sephora=[{  
    'name':'rose gold',
    'type':'eyeshadow plaette',
    'price':25.500

         }]

Mac=[{
    'name':'MAC matte Lipstick',
    'type': 'lipstick',
    'price':7.000
     }]
makeup_forever=[{
     'name':'foundation 118',
     'type': 'invisible cover stick',
     'price':15.000
                 }]

def makeup():
    makeup_choose=input('choose one otion sephora / MAC /makeup forever : ')
    if makeup == ('sephora'):
        return (sephora)
    elif makeup == ('MAC'):
        return (Mac)
    elif makeup == ('makeup forever'):
        return (makeup_forever)
    else:
        return ('erorr')
    
cearaVe={
    'name':'cearaVe SA smothing cleanser',
    'type':'for dry skin',
    'price':5.000
                }

Olay={
    'name':'olay regenerist',
    'typr':'regenerist',
    'price':12.520
}

cetaphill={
    'name':'cetaphill mositurizing cream',
    'type':'mositurizing cream',
    'price':2.435
}
def skincare():
  skincare=input('choose one otion cearaVe/Olay/cetaphill : ')
  if skincare == ('cearaVe'):
      return (cearaVe)
  if skincare == ('Olay'):
      return (Olay)
  if skincare == ('cetaphill'):
      return (cetaphill)
 


def choose1(): 
    choos1 = input('choose one otion makeup / skincare /clothes : ')
    if choos1 == ('mkeupe'):
        return(makeup_brand)
            
    elif choos1 == ('skincare'):
         return(skincare_brand)

    elif choos1 == ('clothes'):
         return(clothes_brand)
    
    else:
        return('error')  

# ==========================

skincare_brand=['cearaVe','Olay','cetaphill']
clothes_brand=['Versace','Zara','Nike']
cars_brand=['BMW','Mercedes-benz','Toyota']

def choose2():
     choos2=input('choose one otion skincare /clothes / cars : ')
     if choos2 == ('skincare'):
         return(skincare_brand)

     elif choos2 == ('clothes'):
         return(clothes_brand)

     elif choos2 == ('cars'):
          return(cars_brand)
     else:
           return('error')

# ==========================

toys_brand=['Lego','toysrus']

skincare_brand2=['Johansons baby', 'QV','seba med']

def choose3():
    choos3=input('choose one otion \toys skincare \clothes : ')
    if choos3 ==('Lego'):
        return(toys_brand)

    elif choos3== ('skincare'):
        return(skincare_brand2)

    elif choos3 == ('clothesc'):
        return(clothes_brand)
    else:
        return('error')

print('hi!welcome to the world store')

print('we need your information to see the products')

name=input('enter your name : ')

print('are you male ?/ female ?/ kid? : ')
gender=input('enter your gander ')

def gender_product(gender1):

    if gender1 == ('female'):
        product_for_female=['makeup','skincare','clothes']
        print(product_for_female)
        return (choose1())

    elif gender1 == ('male'):
        product_for_male=['skincare','clothes','cars']
        print(product_for_male)
        return (choose2())
        

    elif gender1 == ('kid'):
        product_for_kid=['toys','clothes','skincare']
        print(product_for_kid)
        return (choose3())

    else:
       return('erorr')

print(gender_product(gender))

makeup_product=['rose gold','MAC Lipstick','foundation 118']
ephora=('rose gold')
Mac=('MAC Lipstick')
makeup_forever=('foundation 118')


cearaVe=('motisturising lotion')
Olay=('olay natural white')


skincare_product=['motisturising lotion','olay natural white with day dream',]
clothes_product=['Gucci pelted cotton-gabardine trench coat','adelide midi ress in black crepe','essential cropped jacket']


toys_product=['']


lego=('lego harry potter')

toysrus=('bingo game') 

  
         
makeup_product=['rose gold','MAC Lipstick','foundation 118']
skincare_product=['motisturising lotion','olay natural white with day dream']
country=['Kuwait','Saudi Arabia','Oman','Qatar','Bahrain','U.A.U']
user_country=input('entr your country')