import os



def main ():
    from view.view_menu import display_menu;
    from view.view_menu import get_choices;
    from controller.menu import change_page;
    #Configuration Savegarde
    config_file_path_choice = 'save/choice.properties';
    properties_choice = read_properties(config_file_path_choice)

    display_menu()
    choice = get_choices(1,10)
    activate_str = properties_choice.get("activate_money")

    
    change_page(choice,activate_str);
    

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

def save_properties(properties, file_path):
    with open(file_path, 'w') as file:
        for key, value in properties.items():
            file.write(f"{key} = {value}\n")



