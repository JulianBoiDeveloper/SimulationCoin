import os
import sys

from controller.controller_utility import get_file_choice,get_file_lang,get_file_wallet
from view.view_start import view_started


def start ():

    choice_file = get_file_choice()
    translate_file = get_file_lang(choice_file)
    money_file = get_file_wallet()

    #Config Data
    money ={}
    money.update(money_file)
    translate = {
        "welcome" : translate_file.get('welcome').encode('latin1').decode('utf-8'),
        "menu1" : translate_file.get('menu1').encode('latin1').decode('utf-8'),
        "menu2" : translate_file.get('menu2').encode('latin1').decode('utf-8'),
        "menu3" : translate_file.get('menu3').encode('latin1').decode('utf-8'),
        "menu4" : translate_file.get('menu4').encode('latin1').decode('utf-8'),
        "menu5" : translate_file.get('menu5').encode('latin1').decode('utf-8'),
        "menu6" : translate_file.get('menu6').encode('latin1').decode('utf-8'),
        "menu7" : translate_file.get('menu7').encode('latin1').decode('utf-8'),
        "menu8" : translate_file.get('menu8').encode('latin1').decode('utf-8'),
        "menu9" : translate_file.get('menu9').encode('latin1').decode('utf-8'),
        "menu10" : translate_file.get('menu10').encode('latin1').decode('utf-8'),
        "menu11" : translate_file.get('menu11').encode('latin1').decode('utf-8'),
        "enterchoice" : translate_file.get('enterchoice').encode('latin1').decode('utf-8'),
        "invalidchoice" : translate_file.get('invalidchoice').encode('latin1').decode('utf-8'),
        "invalidchoicebetween" : translate_file.get('invalidchoicebetween').encode('latin1').decode('utf-8'),
        "titlechoosecrypto" : translate_file.get('titlechoosecrypto').encode('latin1').decode('utf-8'),
        "errorchoose" : translate_file.get('errorchoose').encode('latin1').decode('utf-8'),
        "menureturn" : translate_file.get('menureturn').encode('latin1').decode('utf-8'),
        "exitprogram" : translate_file.get('exitprogram').encode('latin1').decode('utf-8'),
        "buytitle" : translate_file.get('buytitle').encode('latin1').decode('utf-8')
    }
    choice = {}
    choice.update(choice_file)

    # Return View
    view_started(translate,money,choice)

