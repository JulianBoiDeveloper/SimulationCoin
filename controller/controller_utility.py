import sys
import os

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


def get_choices(min,max,translate):
    choice = None
    while True:
        try:
            choice = int(input(translate["enterchoice"]))   
            if min <= choice <= max:
                return choice
            else:
                print(translate["invalidchoice"])
        except ValueError:
            print(translate["invalidchoicebetween"])

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

