from view.view_sell import sell_crypto;
def change_page(choice):
    match choice:
        case 1: #Choose crypto
           print("Page not found")
           exit;
        case 2: # Buy crypto
           print("Page not found")
           exit;
        case 3: #Sell crypto
           test = sell_crypto()
        case 4: #Crypto per minute
           print("Choix 4")
        case 5: #Crypto per hour
           print("Choix 5")
        case 6: #Crypto per day
           print("Choix 6")
        case 7: #Add to wallet
           print("Choix 7")
        case 8: #Choose currency
           print("Choix 8")
        case 9: #Check account
           print("Choix 9")
        case 10: #Quit
           exit;