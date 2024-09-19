import requests
import time


def cryptobuy(translate,money,choice):
    time.sleep(3) 
    from view.view_buycrypto import view_crypto
    content_first = first_menu(money,choice)
    
    content_last = last_menu(money,choice,content_first)
    view_crypto(translate,content_first,content_last,money,choice)

def first_menu(money,choice):
    selected_money = {}
    for index, (key, value) in enumerate(money.items(), start=1):
        if str(choice["activate_money"]) == str(index):
            selected_money.update({
                "name": str(key)
            })
            
   
    return selected_money

def last_menu(money,choice,money_selected):
    from controller.controller_utility import read_properties
    selected_money = {}
    creditial = read_properties('creditial.properties')


    if 'crypto_available' not in selected_money:
        selected_money['crypto_available'] = []

    data_final = {}

    for index, (key,value) in enumerate(money.items(), start=1):
        if str(choice["activate_money"]) != str(index):
            while True:
                response = requests.get(str(creditial.get("API_URL"))+"data/price?fsym="+str(key)+"&tsyms="+str(money_selected["name"]))
                if response.status_code == 200:
                    data = response.json()
                    if data:
                        data_final.update(data)
                        break 
                    else:
                        print("Données vides, réessayons...")
                        time.sleep(5) 
                else:
                    print("Erreur lors de l'appel API:", response.status_code)
                    break

            selected_money['crypto_available'].append({"name" : key,"conversion":str(data_final[str(money_selected["name"])])})
    
    return selected_money
