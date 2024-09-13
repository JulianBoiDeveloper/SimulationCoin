def view_wallet():
    wallet = {
        "Crypto 1": "somedata",
        "Crypto 2": "somedata",
        "Crypto 3": "somedata"
    }

    print("\nYour Current Wallet:")
    for crypto, amount in wallet.items():
        print(f"{crypto}: {amount:.4f}")

view_wallet()
