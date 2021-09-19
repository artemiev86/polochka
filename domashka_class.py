class Tomato:
    states = {1: "rostok", 2: "kustik", 3: "sozrel"}

    def __init__(self, index):
        self._index = index
        self._state = self.states[1]

    def info(self):
        print(self._state)

    def grow(self):
        if self._state == self.states[1]:
            self._state = self.states[2]
        else:
            self._state = self.states[3]

    def is_ripe(self):
        if self._state == self.states[3]:
            return True
        else:
            return False


class Tomato_Bush:
    def __init__(self, kolichestvo):
        self.tomatoes = []
        for i in range(1, kolichestvo):
            self.tomatoes.append(Tomato(i))

    def grow_all(self):
        for tomat in self.tomatoes:
            tomat.grow()

    def all_are_ripe(self):
        for tomat in self.tomatoes:
            n = tomat.is_ripe()
            return n

    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:
    def __init__(self, name, __plant):
        self.name = name
        self._plant = Tomato(1)

    def work(self):
        self._plant.grow()
    def harvest(self):
        if self.
        