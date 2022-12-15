import csv


def read_file(path_to_file):
    if path_to_file[-4:] != '.csv':
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file, mode='r', encoding='utf-8') as file:
            return list(csv.reader(file))
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def most_requested_dish(orders: list, client: str):
    dishes = [order[1] for order in orders if order[0] == client]
    most_frequent_dish = dishes[0]
    frequency = dict()
    for dish in dishes:
        if dish not in frequency:
            frequency[dish] = 1
        else:
            frequency[dish] += 1
        if frequency[dish] > frequency[most_frequent_dish]:
            most_frequent_dish = dish

    return most_frequent_dish


def amount_this_client_is_dish(orders: list, client: str, dish: str):
    dishes = [
        order[1]
        for order in orders
        if order[0] == client and order[1] == dish
        ]
    return len(dishes)


def dish_that_customer_did_not_order(orders: list, client: str):
    dishes = set(order[1] for order in orders)
    client_dishes = set(order[1] for order in orders if order[0] == client)
    return dishes - client_dishes


def weekdays_that_the_customer_was_not(orders: list, client: str):
    weekdays = set(order[2] for order in orders)
    weekdays_dishes = set(order[2] for order in orders if order[0] == client)
    return weekdays - weekdays_dishes


def analyze_log(path_to_file):
    orders = read_file(path_to_file)
    maria_most_requested_dish = most_requested_dish(orders, 'maria')
    arnaldo_dishes = amount_this_client_is_dish(
        orders, 'arnaldo', 'hamburguer')
    not_ordered_dishes_by_joao = dish_that_customer_did_not_order(
        orders, 'joao')
    joao_ausent_days = weekdays_that_the_customer_was_not(orders, 'joao')

    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(
            f"{maria_most_requested_dish}\n"
            f"{arnaldo_dishes}\n"
            f"{not_ordered_dishes_by_joao}\n"
            f"{joao_ausent_days}\n")
