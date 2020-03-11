
class car:
    # car_type  = ''
    # car_origin = ''
    # car_name = ''
    
    def __init__(self, c_type, c_origin, c_name):
        self.car_type = c_type
        self.car_origin = c_origin
        self.car_name = c_name
        
    def check_car(self):
        return('this car\'s name is  {}'.format(self.car_name))
        
    def check_origin(self):
        return('this is made in {}.format(self.car_orgin')
    
    def check_type(self):
        return('the type of this car is {}'.format(self.car_type))
    
    
benz = car('sedan','germany','s500')

print(benz.car_name)
print(benz.car_origin)
print(benz.car_type)

print(benz.check_car())
print(benz.check_origin())
print(benz.check_type())