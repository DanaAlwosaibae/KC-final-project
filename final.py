#Products and options
sephora = {
    'name': 'rose gold',
    'type': 'eyeshadow palette',
    'price': 25.500
}

Mac = {
    'name': 'MAC matte Lipstick',
    'type': 'lipstick',
    'price': 7.000
}

makeup_forever = {
    'name': 'foundation 118',
    'type': 'invisible cover stick',
    'price': 15.000

}

cearaVe = {
    'name': 'cearaVe SA smoothing cleanser',
    'type': 'for dry skin',
    'price': 5.000
}

Olay = {
    'name': 'olay regenerist',
    'type': 'regenerist',
    'price': 12.520
}

cetaphill = {
    'name': 'cetaphill moisturizing cream',
    'type': 'moisturizing cream',
    'price': 2.435
}
Gucci = {
    'name':'linen and cotton-blend jacqard wide-leg pants',
    'color':'baige',
    'price':'460.000'

}
zara = {
    'name':'short sleeve sweatshirt',
    'price':7.000
}
Nike = {
    'name':'nike ari max',
    'price': 69.000
}

# brands
makeup_brand = ['sephora', 'MAC', 'makeup forever']
skincare_brand = ['cearaVe', 'Olay', 'cetaphill']
clothes_brand = ['Gucci', 'Zara', 'Nike']

# gender categories
def gender_product(gender):
    if gender == 'female':
        product_for_female = ['makeup', 'skincare', 'clothes']
        print(product_for_female)
        return choose1()
    elif gender == 'male':
        product_for_male = ['skincare', 'clothes', 'cars']
        print(product_for_male)
        return choose2()
    else:
        return 'error'
#clothes


#makeup
def makeup():
    makeup_choose = input('choose one option sephora / MAC / makeup forever : ')
    if makeup_choose == 'sephora':
        return sephora
    elif makeup_choose == 'MAC':
        return Mac
    elif makeup_choose == 'makeup forever':
        return makeup_forever
    else:
        return 'error'

#skincare
def skincare():
    skincare_choose = input('choose one option cearaVe / Olay / cetaphill : ')
    if skincare_choose == 'cearaVe':
        return cearaVe
    elif skincare_choose == 'Olay':
        return Olay
    elif skincare_choose == 'cetaphill':
        return cetaphill
    else:
        return 'error'

# female options
def choose1():
    choos1 = input('choose one option makeup / skincare / clothes : ')
    if choos1 == 'makeup':
        return makeup()
    elif choos1 == 'skincare':
        return skincare()
    elif choos1 == 'clothes':
        return clothes_brand
    else:
        return 'error'
#==========================
BMW = {
    'name':'BMW 230i coupe M sport',
    'price':18.900
}
Mercedes_benz = {
    'name':'Mercedes-benz GLB',
    'price':17.100
}
Toyota = {
    'name':'toyota camry',
    'price':10.000
}



# male brands

skincare_brand_male = ['cearaVe', 'Olay', 'cetaphill']
clothes_brand_male = ['Gucci', 'Zara', 'Nike']
cars_brand = ['BMW', 'Mercedes-benz', 'Toyota']

#male options
def choose2():
    choos2 = input('choose one option skincare / clothes / cars : ')
    if choos2 == 'skincare':
        return skincare_brand_male
    elif choos2 == 'clothes':
        return clothes_brand_male
    elif choos2 == 'cars':
        return cars_brand
    else:
        return 'error'


# intro message
print('Hi! Welcome to the World Store')
name = input('Enter your name: ')
print('Are you male? / female? : ')
gender = input('Enter your gender: ')
print(gender_product(gender))
user_country = input('Enter your country: ')


