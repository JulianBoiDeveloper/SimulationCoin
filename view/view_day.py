import daytime

def view_daily():
    crypto_data = {
        "Crypto 1": {"price": "somedata", "volume": "somedata", "change": "somedata"},
        "Crypto 2": {"price": "somedata", "volume": "somedata", "change": "somedata"},
        "Crypto 3": {"price": "somedata", "volume": "somedata", "change": "somedata"},
    }

    today = datetime.date.today()
    
    print(f"Cryptocurrency Information for {today}")
    for crypto, data in crypto_data.items():
        price = f"${data['price']:,.2f}"
        volume = f"{data['volume']:,}"
        change = f"{data['change']:+.2f}%"
        print(f"{crypto}:")
        print(f"  Price: {price}")
        print(f"  Volume: {volume}")
        print(f"  Change: {change}")
        print()

view_daily() 

        