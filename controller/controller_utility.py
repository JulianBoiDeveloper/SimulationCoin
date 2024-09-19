import sys
import os
import datetime
from zoneinfo import ZoneInfo
import locale

def read_properties(file_path):
    properties = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Ignorer les lignes vides et les commentaires
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                properties[key.strip()] = value.strip()
    return properties

def save_properties(properties,path = ""):
    if path == None:
        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.properties')
        with open(file_path, 'w', encoding="utf-8") as file:
            for key, value in properties.items():
                file.write(f"{key} = {value}\n")
    elif path == "":
        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.properties')
        with open(file_path, 'w', encoding="utf-8") as file:
            for key, value in properties.items():
                file.write(f"{key} = {value}\n")
    else:
        with open(path, 'w', encoding="utf-8") as file:
            for key, value in properties.items():
                file.write(f"{key} = {value}\n") 


def get_choices(min,max,translate,money,page,choice_tab):
    from view.view_start import view_started
    from controller.controller_cryptochange import cryptochange
    from controller.controller_buycrypto import cryptobuy
    choice = None
    while True:
        try:
            choice = int(input(translate["enterchoice"]))   
            if min <= choice <= max:
                return choice
            else:
                print(translate["invalidchoice"])
                if page == 1:
                    view_started(translate,money,choice_tab)
                elif page == 2:
                    cryptochange(translate,money,choice_tab)
                elif page == 3:
                    cryptobuy(translate,money,choice_tab)
                else:
                    raise Exception("This page doen't exist.")
        except ValueError:
            print(translate["invalidchoicebetween"])
            if page == 1:
                view_started(translate,money,choice_tab)
            elif page == 2:
                cryptochange(translate,money,choice_tab)
            elif page == 3:
                    cryptobuy(translate,money,choice_tab)
            else:
                raise Exception("This page doen't exist.")

def get_file_choice():
    # Configuration Choix
    try:
        path_choice_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.properties')
        choice_file =  read_properties(path_choice_file)
        return choice_file
    except FileNotFoundError:
        print("[CRITICAL] The configuration file 'config.properties' does not have the required data. Please make sure to change that.")
        sys.exit()

def get_file_lang(choice_file):
    #Configuration Langage
    try:
        path_translate_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lang', choice_file.get("lang")+'.properties')
        translate_file = read_properties(path_translate_file)
        return translate_file
    except FileNotFoundError:
        print("[CRITICAL] The configuration properties file does not have the required language. Please make sure to change that.")
        sys.exit()
    except TypeError:
        print("[CRITICAL] The configuration file 'config.properties' does not have the required data. Please make sure to change that.")
        sys.exit()
def get_file_wallet():
    # Configuration Money
    try:
        path_money_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config/wallet', 'config.properties')
        money_file =  read_properties(path_money_file)
        return money_file
    except FileNotFoundError:
        print("[CRITICAL] The configuration properties file does not have the required language. Please make sure to change that.")
        sys.exit()

def epoch_to_time(epoch_time):
    choice_file = get_file_choice()
    locale.setlocale(locale.LC_TIME, str(choice_file["locale"])+'.UTF-8')
    dt_utc = datetime.datetime.fromtimestamp(epoch_time, tz=datetime.timezone.utc)
    # Convertir le datetime UTC au fuseau horaire local avec zoneinfo
    local_time = dt_utc.astimezone(ZoneInfo(str(choice_file["timezone"])))
    # Formater le datetime
    formatted_date = local_time.strftime('%A %d %B - %H:%M:%S')
    return str(formatted_date).capitalize()

def get_money_input():
    from view.view_start import view_started
    from controller.controller_cryptochange import cryptochange
    from controller.controller_buycrypto import cryptobuy
    choice = None
    while True:
        try:
            choice = int(input(translate["enterchoice"]))   
            if min <= choice <= max:
                return choice
            else:
                print(translate["invalidchoice"])
                if page == 1:
                    view_started(translate,money,choice_tab)
                elif page == 2:
                    cryptochange(translate,money,choice_tab)
                elif page == 3:
                    cryptobuy(translate,money,choice_tab)
                else:
                    raise Exception("This page doen't exist.")
        except ValueError:
            print(translate["invalidchoicebetween"])
            if page == 1:
                view_started(translate,money,choice_tab)
            elif page == 2:
                cryptochange(translate,money,choice_tab)
            elif page == 3:
                    cryptobuy(translate,money,choice_tab)
            else:
                raise Exception("This page doen't exist.")