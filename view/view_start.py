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
    form_start(translate,money,choice)

def form_start(translate,money,choice):
    from controller.controller_cryptochange import cryptochange
    from controller.controller_buycrypto import cryptobuy
    selected = get_choices(1,11,translate,money,1,choice)
    if selected == 1:
        cryptochange(translate,money,choice)
    elif selected == 2:
        cryptobuy(translate,money,choice)
    elif selected == 11:
        print(translate["exitprogram"])
        sys.exit()
    else:
        print(translate["invalidchoice"])
        view_started(translate,money,choice)
    