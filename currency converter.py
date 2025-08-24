def currency_converter():
    print("💱 Simple Currency Converter")
    print("Available conversions: ")
    print("1. INR ➝ USD")
    print("2. USD ➝ INR")
    print("3. INR ➝ EUR")
    print("4. EUR ➝ INR")

    choice = int(input("Enter your choice (1-4): "))
    amount = float(input("Enter the amount: "))

    # fixed rates (for demo purpose)
    inr_to_usd = 0.012
    usd_to_inr = 83.0
    inr_to_eur = 0.011
    eur_to_inr = 90.0

    if choice == 1:
        print(f"{amount} INR = {amount * inr_to_usd:.2f} USD")
    elif choice == 2:
        print(f"{amount} USD = {amount * usd_to_inr:.2f} INR")
    elif choice == 3:
        print(f"{amount} INR = {amount * inr_to_eur:.2f} EUR")
    elif choice == 4:
        print(f"{amount} EUR = {amount * eur_to_inr:.2f} INR")
    else:
        print("❌ Invalid choice")

currency_converter()
