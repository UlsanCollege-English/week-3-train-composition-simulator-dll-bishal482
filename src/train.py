# src/train.py

class Train:
    def __init__(self):
        self.cars = []

    def attach_back(self, car_id):
        self.cars.append(car_id)

    def attach_front(self, car_id):
        self.cars.insert(0, car_id)

    def detach_front(self):
        if not self.cars:
            return None
        return self.cars.pop(0)

    def detach_back(self):
        if not self.cars:
            return None
        return self.cars.pop()

    def detach(self, car_id):
        if car_id in self.cars:
            self.cars.remove(car_id)
            return True
        return False

    def to_list(self):
        return self.cars.copy()
