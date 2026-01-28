import argparse
import os
from bot.client import BinanceClient
from bot.orders import OrderService

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    API_KEY = os.getenv("BINANCE_API_KEY")
    API_SECRET = os.getenv("BINANCE_API_SECRET")

    if not API_KEY or not API_SECRET:
        print("Set BINANCE_API_KEY and BINANCE_API_SECRET env variables")
        return

    client = BinanceClient(API_KEY, API_SECRET)
    service = OrderService(client)

    print("\n--- Order Summary ---")
    print(vars(args))

    try:
        result = service.create_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("\n--- Order Response ---")
        print(f"Order ID: {result['orderId']}")
        print(f"Status: {result['status']}")
        print(f"Executed Qty: {result['executedQty']}")
        print(f"Avg Price: {result.get('avgPrice', 'N/A')}")


        print("\n✅ Order placed successfully")

    except Exception as e:
        print("\n❌ Order failed:", str(e))


if __name__ == "__main__":
    main()
