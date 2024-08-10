class ParkingSystem:
    def __init__(self, big, medium, small):
        self.big_spaces = big
        self.medium_spaces = medium
        self.small_spaces = small
        
    def add_car(self, car_type):
        if car_type == 1:
            if self.big_spaces <= 0:
                return False
            else:
                self.big_spaces -= 1
                return True
        elif car_type == 2:
            if self.medium_spaces <= 0:
                return False
            else:
                self.medium_spaces -= 1
                return True
        elif car_type == 3:
            if self.small_spaces <= 0:
                return False
            else:
                self.small_spaces -= 1
                return True

        return None
