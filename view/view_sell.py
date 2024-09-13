def sell_crypto():
    wallet = {
        "Crypto 1": "somedata",
        "Crypto 2": "somedata",
        "Crypto 3": "somedata"
    }
    
    crypto_prices = {
        "Crypto 1": "somedata",
        "Crypto 2": "somedata",
        "Crypto 3": "somedata"
    }

    print("\nYour Current Wallet:")
    for crypto, amount in wallet.items():
        print(f"{crypto}: {amount:.4f}")

    crypto_to_sell = input("\nEnter the name of the cryptocurrency you want to sell: ")
    
    if crypto_to_sell not in wallet:
        print("You don't have this cryptocurrency in your wallet.")
        return

    max_amount = wallet[crypto_to_sell]
    amount_to_sell = float(input(f"Enter the amount of {crypto_to_sell} you want to sell (max {max_amount:.4f}): "))

    if amount_to_sell > max_amount:
        print("You don't have enough of this cryptocurrency.")
        return

    sale_value = amount_to_sell * crypto_prices[crypto_to_sell]
    
    wallet[crypto_to_sell] -= amount_to_sell

    print(f"\nYou sold {amount_to_sell:.4f} {crypto_to_sell} for ${sale_value:.2f}")
    print("\nUpdated Wallet:")
    for crypto, amount in wallet.items():
        print(f"{crypto}: {amount:.4f}")

sell_crypto()
