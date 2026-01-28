from .validators import *
from .logging_config import setup_logger

logger = setup_logger()

class OrderService:
    def __init__(self, client):
        self.client = client

    def create_order(self, symbol, side, order_type, quantity, price=None):

        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(price, order_type)

        order_data = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            order_data["price"] = price
            order_data["timeInForce"] = "GTC"

        logger.info(f"Order Request: {order_data}")

        try:
            response = self.client.place_order(**order_data)
            logger.info(f"Order Response: {response}")
            return response

        except Exception as e:
            logger.error(f"API Error: {str(e)}")
            raise
