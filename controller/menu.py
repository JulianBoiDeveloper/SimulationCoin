import os

from controller.before_menu import read_properties
from controller.before_menu import save_properties

config_file_path_choice = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'save', 'choice.properties')
properties_choice = read_properties(config_file_path_choice)

lang = properties_choice.get("lang")

def change_page(choice,activate):
      from controller.coin_change import get_page_change;
      if(activate != "4"):
            properties ={
                  "lang": lang,
                  "activate_money" : activate
            }
            save_properties(properties, config_file_path_choice)
      match choice:
            case 1: #Choose crypto
                  get_page_change(activate)
            case 10: #Quit
                  exit;