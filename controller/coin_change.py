import os

from controller.before_menu import read_properties

from view.view_menu import get_choices;


#Configuration Internationalisation
config_file_path_choice = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'save', 'choice.properties')
properties_choice = read_properties(config_file_path_choice)

#Configuration Internationalisation
config_file_path_internationnalisation = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'lang', properties_choice.get("lang")+'.properties')
properties_inter = read_properties(config_file_path_internationnalisation)



from controller.wallet import current_wallet;
from controller.menu import change_page;
from controller.before_menu import main


btc,eth,ltc = current_wallet()



def get_page_change(activate):
    print(properties_inter.get('titlechoosecrypto'))
    if activate == "1":
        print("1. *"+properties_inter.get('money1') + " : " + str(btc))
        print("2. " +properties_inter.get('money2')+ " : " + str(ltc))
        print("3. " +properties_inter.get('money3')+ " : " + str(eth))
        print("------------")
        print("4. " + properties_inter.get('menureturn'))
        activate = str(get_choices(1,4))
        change_page(1,activate)
    elif activate == "2":
        print("1. " +properties_inter.get('money1')+ " : " + str(btc))
        print("2. *"+properties_inter.get('money2')+ " : " + str(ltc))
        print("3. " +properties_inter.get('money3')+ " : " + str(eth))
        print("------------")
        print("4. " + properties_inter.get('menureturn'))
        activate = str(get_choices(1,4))
        change_page(1,activate)
    elif activate == "3":
        print("1. " +properties_inter.get('money1')+ " : "+ str(btc))
        print("2. " +properties_inter.get('money2')+ " : " + str(ltc))
        print("3. *"+ properties_inter.get('money3')+ " : " + str(eth))
        print("------------")
        print("4. " + properties_inter.get('menureturn'))
        activate = str(get_choices(1,4))
        change_page(1,activate)
    else:
        main()