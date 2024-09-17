import os

from controller.before_menu import read_properties

#Configuration Internationalisation
config_file_path_choice = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'save', 'choice.properties')
properties_choice = read_properties(config_file_path_choice)

#Configuration Internationalisation
config_file_path_internationnalisation = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lang', properties_choice.get("lang")+'.properties')
properties_inter = read_properties(config_file_path_internationnalisation)


# Affichage du menu
def display_menu():
    print(properties_inter.get('welcome'))
    print(properties_inter.get('menu1'))
    print(properties_inter.get('menu2'))
    print(properties_inter.get('menu3'))
    print(properties_inter.get('menu4'))
    print(properties_inter.get('menu5'))
    print(properties_inter.get('menu6'))
    print(properties_inter.get('menu7'))
    print(properties_inter.get('menu8'))
    print(properties_inter.get('menu9'))
    print(properties_inter.get('menu10'))

# Change option
def get_choices(min,max):
    while True:
        try:
            choice = int(input(properties_inter.get('enterchoice')))    
            if min <= choice <= max:
                return choice
            else:
                print(properties_inter.get('invalidchoice'))
        except ValueError:
            print(properties_inter.get('invalidchoicebetween'))

