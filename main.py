import json


def process_hotel_data(data):
    """
    Process hotel data to find the cheapest price, associated room type, number of guests,
    and calculate total prices for all rooms.

    Args:
        data (dict): JSON data containing hotel information.

    Returns:
        dict: Dictionary containing the cheapest room price, room type, number of guests,
              and total prices for all rooms.
    """
    hotel_data = data['assignment_results'][0]
    shown_prices = hotel_data['shown_price']
    net_prices = hotel_data['net_price']
    number_of_guests = hotel_data['number_of_guests']

    cheapest_price = None
    cheapest_room_type = None

    for room_type, price_str in shown_prices.items():
        price = float(price_str)
        if (cheapest_price is None) or (price < cheapest_price):
            cheapest_price = price
            cheapest_room_type = room_type

    taxes = json.loads(hotel_data['ext_data']['taxes'])
    total_tax = sum(float(tax) for tax in taxes.values())

    total_prices = []
    for room_type, net_price_str in net_prices.items():
        net_price = float(net_price_str)
        total_price = net_price + total_tax
        total_prices.append({
            'room_type': room_type,
            'total_price': round(total_price, 2)
        })

    result = {
        'cheapest_room': {
            'price': cheapest_price,
            'room_type': cheapest_room_type,
            'guests': number_of_guests
        },
        'total_prices': total_prices
    }

    return result


def main():
    with open('Python-task.json', 'r') as file:
        data = json.load(file)

    result = process_hotel_data(data)

    with open('analysis_output.json', 'w') as file:
        json.dump(result, file, indent=4)


if __name__ == "__main__":
    main()
