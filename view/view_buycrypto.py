import datetime

from controller.controller_utility import epoch_to_time

def view_crypto(translate,content_first,content_last,money,choice):
    print(translate["buytitle"] +" ("+translate["titlechoosecrypto"] +" "+ str(money[str(content_first.get("name"))]) +" "+ str(content_first.get("name")) +")")
    index = 0
    for crypto in content_last.get("crypto_available"):
        index += 1
        conversion  = f"{float(crypto["conversion"]):.8f}"
        print("--------------"+str(index) +"----------- 1 " + str(crypto["name"]) + " ~=  " + str(conversion) +" "+ str(content_first.get("name")) + " en date du : " + epoch_to_time(int(datetime.datetime.now().timestamp())))
    index+=1
    print("--------------"+str(index) +"----------- "+ translate["menureturn"])
    print(translate["cryptomenuoption"])
    form_buy_crypto(1,index,translate,money,3,choice,content_first,content_last,choice)

def form_buy_crypto(min,max,translate,money,page,choice_tab,content_first,content_last,choice):
    from controller.controller_utility import get_choices
    from view.view_start import view_started
    choice_buy_crypto = get_choices(min,max,translate,money,page,choice_tab)
    if str(choice_buy_crypto) == str(max):
        view_started(translate,money,choice_tab)
    else:
        print(translate["cryptomenuoptionamount1"] +" "+ str(content_first.get("name")) +" "+ translate["to"] +" "+ content_last.get("crypto_available")[int(choice_buy_crypto-1)]["name"] +" "+ translate["cryptomenuoptionamount2"])
        choice_buy_amount_crypto = input(str(translate["chooseamountcryptobuy"])+ " ")

        if choice_buy_amount_crypto == 0:
            view_crypto(translate,content_first,content_last,money,choice)
        else:
            
            # choice_buy_amount_crypto = 
            # for carte in cartes:
            #     if choice_buy_amount_crypto > carte[""]
            #         print("Montant insuffisant sur la carte"choice_buy_amount_crypto)





