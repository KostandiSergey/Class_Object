class Bird:

    def __init__(self, range_flight, flight_altitude, stomach_capacity):
        self.range_flight = range_flight
        self.flight_altitude = flight_altitude
        self.stomach_capacity = stomach_capacity

    def display_max_range(self):
        # Отобразим макс растояние на которое птичка сможет пролететь.
        print(
            f"На данный момент максимальная дальнасть полета: {self.range_flight}"
        )

    def set_max_range(self, range_flight):
        # установим до какого расстояния дотянет наша птичка пока есть топливо.
        self.range_flight = range_flight

    def display_max_altitude(self):
        # Отобразим где сейчас летает наша птичка.
        print(
            f"На данный момент птичка находится на высоте: {self.flight_altitude}"
        )

    def set_max_flight_altitude(self, flight_altitude):
        # Установим на какую максимальную высоту птичка может взлететь за один раз.
        self.flight_altitude = flight_altitude

    def get_stomach_capacity(self, stomach_capacity):
        # Установим сколько топлива может вместиться в птичку.
        self.stomach_capacity = stomach_capacity

    def show_stomach_capacity(self):
        # Обьем желудка показывает какое кол-во топливо вместиться в птичку.
        print(
            f"Обьем желудка для этой птичке равен: {self.stomach_capacity}"
        )

    def start_fly(self):
        # Каждый раз, когда птичка взлетает, то ее обьем желудка должен уменьшеться на 1. (вариант лучшего описания коммента)
        # Потому что птица тратит много энергии на свой полет.
        # Хороший комментарий должен обьяснить логику функции.
        self.stomach_capacity -= 1
        print("к взлету!")


tangerine = Bird(100, 500, 5)
magpie = Bird(50, 300, 3)
raven = Bird(75, 200, 4)

tangerine.display_max_range()
print(raven.__dict__)
magpie.set_max_range(1000)
magpie.display_max_range()