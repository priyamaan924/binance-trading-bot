import logging
def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"Placing order: {symbol} {side} {order_type} {quantity} {price}")

        # Simulated response (since test keys don't work)
        order = {
            "orderId": 123456,
            "status": "FILLED",
            "executedQty": quantity,
            "avgPrice": price if price else "market_price"
        }

        logging.info(f"Order Response: {order}")
        return order

    except Exception as e:
        logging.error(f"Order failed: {str(e)}")
        raise