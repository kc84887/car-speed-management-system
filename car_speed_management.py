class Car:

    def __init__(self, speed):
        self.current_speed = speed
        
    
    def accelerate(self, value):
        self.current_speed += value
        print("Show current speed after accelerate = ", self.get_speed())

    def brake(self, value):
        self.current_speed -= value
        print("Show current speed after brake = ", self.get_speed())

    def get_speed(self):
        return self.current_speed
    
s1 = Car(1000) 

s1.accelerate(400)                                                                                                                          
s1.brake(200)



