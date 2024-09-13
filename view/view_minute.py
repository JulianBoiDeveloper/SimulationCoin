import datetime

now = datetime.datetime.now()


def view_hourly():
    crypto_data = {
        "Crypto 1": {"price": 3000, "volume": 50000, "change": 0.5},
        "Crypto 2": {"price": 150, "volume": 25000, "change": -0.2},
        "Crypto 3": {"price": 50, "volume": 100000, "change": 0.1},
    }

    now = datetime.datetime.now()
    
    print(f"Cryptocurrency Information for {now.minute}:00")
    for crypto, data in crypto_data.items():
        price = f"${data['price']:,.2f}"
        volume = f"{data['volume']:,}"
        change = f"{data['change']:+.2f}%"
        print(f"{crypto}:")
        print(f"  Price: {price}")
        print(f"  Volume: {volume}")
        print(f"  Change: {change}")
        print()

view_hourly()