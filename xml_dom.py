import xml.dom.minidom

domtree = xml.dom.minidom.parse('simple.xml')
breakfast = domtree.documentElement

foods = breakfast.getElementsByTagName('food')

for food in foods:
    print('-----FOOD-----')
    if food.hasAttribute('id'):
        print("ID: {}".format(food.getAttribute('id')))

    print("NAME: {}".format(food.getElementsByTagName('name')[0].childNodes[0].data))
    print("PRICE: {}".format(food.getElementsByTagName('price')[0].childNodes[0].data))
    print("DESCRIPTION: {}".format(food.getElementsByTagName('description')[0].childNodes[0].data))
    print("CALORIES: {}".format(food.getElementsByTagName('calories')[0].childNodes[0].data))

newfood = domtree.createElement('food')
newfood.setAttribute('id', '0')

name = domtree.createElement('name')
name.appendChild(domtree.createTextNode('Name'))

price = domtree.createElement('price')
price.appendChild(domtree.createTextNode('Price'))

description = domtree.createElement('description')
description.appendChild(domtree.createTextNode('Description'))

calories = domtree.createElement('calories')
calories.appendChild(domtree.createTextNode('Calories'))

newfood.appendChild(name)
newfood.appendChild(price)
newfood.appendChild(description)
newfood.appendChild(calories)

breakfast.appendChild(newfood)

domtree.writexml(open('simple.xml', 'w'))