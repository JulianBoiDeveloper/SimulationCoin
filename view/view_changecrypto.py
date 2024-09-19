from controller.controller_utility import get_choices


def view_changecrypto(translate,money,choice):
    print("--------------------------------------------------------")
    print(translate["titlechoosecrypto"])
    count = 0
    cursor_final = len(money)+1
    for index, (key, value) in enumerate(money.items(), start=1):
        count = count +1
        if str(count) == str(choice["activate_money"]):
            print(str(index) + ". " + "(*)" +   key+" : "+value)
        else:
            print(str(index) + ". " +"( )" +  key+" : "+value)
    print(str(cursor_final)+". "+translate["menureturn"])
    form_changecrypto(translate,cursor_final,money,choice)

def form_changecrypto(translate,max,money,choice):
    from controller.controller_cryptochange import cryptoselected
    selected = get_choices(1,max,translate)
    cryptoselected(selected,translate,money,choice,max)

def reset_samecrypto(translate,money,choice):
    from controller.controller_cryptochange import cryptochange
    print("--------------------------------------------------------")
    print("Déja selectionné")
    cryptochange(translate,money,choice)
    

    
