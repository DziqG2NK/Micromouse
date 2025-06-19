class Direction:
    def __init__(self, value):
        if isinstance(value, str):
            value = {'UP': 0, 'RIGHT': 1, 'DOWN': 2, 'LEFT': 3}[value]
        elif isinstance(value, int):
            value = value % 4
        else:
            raise ValueError("Direction value must be an int or str")

        self.value = value

    def get_value(self):
        return self.value

    def __add__(self, other):
        if isinstance(other, Direction):
            return Direction(self.value + other.value)
        elif isinstance(other, int):
            return Direction(self.value + other)
        elif isinstance(other, str):
            return Direction(self.value + {'UP': 0, 'RIGHT': 1, 'DOWN': 2, 'LEFT': 3}[other])
        else:
            raise TypeError("Can only add Direction or int to Direction")

    def __radd__(self, other):
        if isinstance(other, Direction):
            return Direction(other.value + self.value)
        elif isinstance(other, int):
            return Direction(other + self.value)
        elif isinstance(other, str):
            return Direction({'UP': 0, 'RIGHT': 1, 'DOWN': 2, 'LEFT': 3}[other] + self.value)
        else:
            raise TypeError("Can only add Direction or int to Direction")

    def __sub__(self, other):
        if isinstance(other, Direction):
            return Direction(self.value - other.value)
        elif isinstance(other, int):
            return Direction(self.value - other)
        elif isinstance(other, str):
            return Direction(self.value - {'UP': 0, 'RIGHT': 1, 'DOWN': 2, 'LEFT': 3}[other])
        else:
            raise TypeError("Can only subtract Direction or int from Direction")

    def __rsub__(self, other):
        if isinstance(other, Direction):
            return Direction(other.value - self.value)
        elif isinstance(other, int):
            return Direction(other - self.value)
        elif isinstance(other, str):
            return Direction({'UP': 0, 'RIGHT': 1, 'DOWN': 2, 'LEFT': 3}[other] - self.value)
        else:
            raise TypeError("Can only subtract Direction or int from Direction")

    def __eq__(self, other):
        if isinstance(other, Direction):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other % 4
        elif isinstance(other, str):
            return self.value == {'UP': 0, 'RIGHT': 1, 'DOWN': 2, 'LEFT': 3}[other]
        else:
            return False

    def __repr__(self):
        direction_map = {0: 'UP', 1: 'RIGHT', 2: 'DOWN', 3: 'LEFT'}
        return f"Direction('{direction_map[self.value]}')"
