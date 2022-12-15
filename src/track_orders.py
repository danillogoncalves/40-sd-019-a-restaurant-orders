class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.orders = list()
        self._custormesr = set()
        self._dishes = set()
        self._weekdays = set()

    def __len__(self):
        return len(self.orders)

    def every_weekday_worked(self):
        return [
            order['weekday']
            for order in self.orders
        ]

    def most_frequently(self, list: list):
        most_common_item = list[0]
        frequency = dict()
        for item in list:
            if item not in frequency:
                frequency[item] = 1
            else:
                frequency[item] += 1
            if frequency[item] > frequency[most_common_item]:
                most_common_item = item

        return most_common_item

    def less_frequent(self, list: list):
        most_common_item = list[0]
        frequency = dict()
        for item in list:
            if item not in frequency:
                frequency[item] = 1
            else:
                frequency[item] += 1
            if frequency[item] < frequency[most_common_item]:
                most_common_item = item

        return most_common_item

    def add_new_order(self, customer, order, day):
        self.orders.append({
            "customer": customer,
            "dish": order,
            "weekday": day
            })
        self._custormesr.add(customer)
        self._dishes.add(order)
        self._weekdays.add(day)

    def get_most_ordered_dish_per_customer(self, customer):
        dishes = [
            order['dish']
            for order in self.orders
            if order['customer'] == customer
        ]

        return self.most_frequently(dishes)

    def get_never_ordered_per_customer(self, customer):
        dishes = set(
            order['dish']
            for order in self.orders
            if order['customer'] == customer
        )

        return self._dishes - dishes

    def get_days_never_visited_per_customer(self, customer):
        weekdays = set(
            order['weekday']
            for order in self.orders
            if order['customer'] == customer
        )

        return self._weekdays - weekdays

    def get_busiest_day(self):
        every = self.every_weekday_worked()

        return self.most_frequently(every)

    def get_least_busy_day(self):
        every = self.every_weekday_worked()

        return self.less_frequent(every)
