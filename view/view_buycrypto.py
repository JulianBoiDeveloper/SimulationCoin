import datetime

from controller.controller_utility import epoch_to_time

def view_crypto(translate,content_first,content_last,money,choice):
    print(translate["buytitle"] +" "+ content_first.get("name"))
    index = 0
    for crypto in content_last.get("crypto_available"):
        index += 1
        conversion  = f"{float(crypto["conversion"]):.8f}"
        print("--------------"+str(index) +"----------- 1 " + str(crypto["name"]) + " ~=  " + str(conversion) +" "+ str(content_first.get("name")) + " en date du : " + epoch_to_time(int(datetime.datetime.now().timestamp())))
    index+=1
    print("--------------"+str(index) +"----------- Retour au menu")
    print("Mettez le numéro de la crypto ou retour au menu")
    form_buy_crypto(1,index,translate,money,2,choice)

def form_buy_crypto(min,max,translate,money,page,choice_tab):
    from controller.controller_utility import get_choices
    choice_buy_crypto = get_choices(min,max,translate,money,page,choice_tab)
    print(choice_buy_crypto)




