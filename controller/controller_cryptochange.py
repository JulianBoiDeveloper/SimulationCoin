import os
import sys

from controller.controller_utility import save_properties


def cryptochange(translate,money,choice):
    from view.view_changecrypto import view_changecrypto    
    view_changecrypto(translate,money,choice)

def cryptoselected(selected,translate,money,choice,max):
    from view.view_changecrypto import reset_samecrypto
    from view.view_start import view_started
    if selected < max:
        if str(selected) == str(choice["activate_money"]):
            reset_samecrypto(translate,money,choice)
        else:
            choice_final = {}
            choice_final.update(choice)
            choice_final["activate_money"] = selected
            save_properties(choice_final)
            cryptochange(translate,money,choice_final)
    else:
        if selected == max:
            view_started(translate,money,choice)
        else:
            print("--------------------------------------------------------")
            print(translate["errorchoose"])
            cryptochange(translate,money,choice)