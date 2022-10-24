#JDU SKINS ADDER BY Just gemer
import os
print("JDU SKINS ADDER BY Just gemer")
jdver = str(input("jdVersion: "))
price = str(input("mojoPrice(type 0 if you dont want it): "))
unlock = str(input("unlockType: "))
url = str(input("url: "))
num = str(input("skin number: "))

# Skins Adder 
skin = open("skins.json", "w", encoding="utf-8")
skin.write('''{
    "''' + num + '''": {
        "__class": "OnlineCustomizableItem",
        "jdVersion": ''' + jdver + ''',
        "mojoPrice": ''' + price + ''',
        "status": 3,
        "unlockType": ''' + unlock + ''',
        "url": "''' + url + '''",
        "itemType": 1,
        "visibility": 1
    }
}''')
skin.close()
