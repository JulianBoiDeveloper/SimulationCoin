import sys
from controller.controller_utility import get_choices

def view_started(translate,money,choice):
    print(translate["welcome"])
    print(translate["menu1"])
    print(translate["menu2"])
    print(translate["menu3"])
    print(translate["menu4"])
    print(translate["menu5"])
    print(translate["menu6"])
    print(translate["menu7"])
    print(translate["menu8"])
    print(translate["menu9"])
    print(translate["menu10"])
    print(translate["menu11"])
    form_start(translate,money,choice)

def form_start(translate,money,choice):
    from model.cb import CarteBancaire
    cartes ={
        "1" : CarteBancaire("Dupont.F","1234 5678 9101 1121","12/31","275",675724.57),
        "2" : CarteBancaire("Hervé.H","4532 8723 9987 3456","10/27","148",24.00),
        "3" : CarteBancaire("Alteros.B","5567 1122 3366 7788","04/29","921",6200.00)
    }

    from controller.controller_cryptochange import cryptochange
    from controller.controller_buycrypto import cryptobuy
    selected = get_choices(1,11,translate,money,1,choice)
    if selected == 1:
        cryptochange(translate,money,choice)
    elif selected == 2:
        cryptobuy(translate,money,choice,cartes)
    elif selected == 11:
        print(translate["exitprogram"])
        sys.exit()
    else:
        print(translate["invalidchoice"])
        view_started(translate,money,choice)
    