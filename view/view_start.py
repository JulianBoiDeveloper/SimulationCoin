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
    from controller.controller_cryptochange import cryptochange
    selected = get_choices(1,11,translate)
    if selected == 1:
        cryptochange(translate,money,choice)
    elif selected == 2:
        return 2;
    else:
        view_started(translate)
    