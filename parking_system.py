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

# Test cases

print('Instantiating new object...')
obj = ParkingSystem(0, 0, 2)
print('...done.')

print(f'---')
print(f'Number of spaces for big cars: {obj.big_spaces}')
print(f'Number of spaces for medium-sized cars: {obj.medium_spaces}')
print(f'Number of spaces for small cars: {obj.small_spaces}')
print(f'---')

print(f'Attempting to add a big car...')
param_1 = obj.add_car(1)
print(f'Success.') if param_1 else print(f'Not enough spaces.')

print(f'Attempting to add a medium-sized car...')
param_2 = obj.add_car(2)
print(f'Success.') if param_2 else print(f'Not enough spaces.')

print(f'Attempting to add a small car...')
param_3 = obj.add_car(3)
print(f'Success.') if param_3 else print(f'Not enough spaces.')

print(f'------------------------------------------------')

print('Instantiating new object...')
obj = ParkingSystem(1, 1, 0)
print('...done.')

print(f'---')
print(f'Number of spaces for big cars: {obj.big_spaces}')
print(f'Number of spaces for medium-sized cars: {obj.medium_spaces}')
print(f'Number of spaces for small cars: {obj.small_spaces}')
print(f'---')

print(f'Attempting to add a big car...')
param_1 = obj.add_car(1)
print(f'Success.') if param_1 else print(f'Not enough spaces.')

print(f'Attempting to add a medium-sized car...')
param_2 = obj.add_car(2)
print(f'Success.') if param_2 else print(f'Not enough spaces.')

print(f'Attempting to add a small car...')
param_3 = obj.add_car(3)
print(f'Success.') if param_3 else print(f'Not enough spaces.')

print(f'Attempting to add a big car...')
param_4 = obj.add_car(1)
print(f'Success.') if param_4 else print(f'Not enough spaces.')
