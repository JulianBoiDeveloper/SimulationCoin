import datetime

def view_details(currency='USD'):
    crypto_data = {
        "Bitcoin": {"price_usd": "somedata", "price_eur": "somedata", "volume": "somedata", "change": "somedata"},
        "Ethereum": {"price_usd": "somedata", "price_eur": "somedata", "volume": "somedata", "change": "somedata"},
        "Dogecoin": {"price_usd": "somedata", "price_eur": "somedata", "volume": "somedata", "change": "somedata"},
    }

    for crypto, data in crypto_data.items():
        price = data[f'price_{currency.lower()}']
        price_formatted = f"${price:,.2f}" if currency == 'USD' else f"€{price:,.2f}"
        volume = f"{data['volume']:,}"
        change = f"{data['change']:+.2f}%"
        
        print(f"{crypto}:")
        print(f"  Price: {price_formatted}")
        print(f"  Volume: {volume}")
        print(f"  24h Change: {change}")
        print()

def choose_currency():
    while True:
        currency = input("Choose currency (USD/EUR): ").upper()
        if currency in ['USD', 'EUR']:
            return currency
        else:
            print("Invalid choice. Please enter USD or EUR.")

def view_crypto_details():
    currency = choose_currency()
    view_details(currency)

if __name__ == "__main__":
    view_details()
