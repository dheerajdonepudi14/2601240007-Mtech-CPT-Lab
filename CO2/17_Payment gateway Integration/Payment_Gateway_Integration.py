# Q17. Payment Gateway Integration
# EAFP (Easier to Ask for Forgiveness than Permission)


class GatewayA:
    """Payment gateway that provides the pay() API."""

    def pay(self, amount):
        return f"GatewayA: Payment of ₹{amount:.2f} successful"


class GatewayB:
    """Payment gateway that uses a different API and has no pay() method."""

    def process_payment(self, amount):
        return f"GatewayB: Payment of ₹{amount:.2f} successful"


class GatewayC:
    """Payment gateway that provides the pay() API."""

    def pay(self, amount):
        return f"GatewayC: Payment of ₹{amount:.2f} successful"


def make_payment(gateway, amount):
    """Process payment using the EAFP approach.

    EAFP directly attempts the required operation and handles
    AttributeError if the gateway does not provide the pay() API.
    """
    try:
        return gateway.pay(amount)
    except AttributeError:
        return "Payment failed: this gateway does not provide the pay() API."


def main():
    print("\n--- PAYMENT GATEWAY INTEGRATION ---")
    print("1. GatewayA (supports pay())")
    print("2. GatewayB (does not support pay())")
    print("3. GatewayC (supports pay())")

    choice = int(input("Enter gateway choice: "))
    amount = float(input("Enter payment amount: ₹"))

    gateways = {
        1: GatewayA(),
        2: GatewayB(),
        3: GatewayC()
    }

    gateway = gateways.get(choice)

    if gateway is None:
        print("Invalid gateway choice.")
        return

    print(make_payment(gateway, amount))


if __name__ == "__main__":
    main()
