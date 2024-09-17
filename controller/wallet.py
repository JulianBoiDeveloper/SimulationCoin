import os

from controller.before_menu import read_properties


#Configuration Internationalisation
config_file_path_wallet = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'wallet', 'wallet.properties')
properties_wallet = read_properties(config_file_path_wallet)

def current_wallet():
    return properties_wallet.get('btc'),properties_wallet.get('eth'),properties_wallet.get('ltc')