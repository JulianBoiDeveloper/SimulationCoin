def crypto_list():
    cryptocurrencies = [
        "Bitcoin (BTC)",
        "Ethereum (ETH)",
    ]
    
    print("List of Cryptocurrencies:")
    for index, crypto in enumerate(cryptocurrencies, 1):
        print(f"{index}. {crypto}")

crypto_list()