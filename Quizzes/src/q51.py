class Wheel:
    def __init__(self,wheel_size:int,frame_material:str):
        self.size = wheel_size*2.54
        self.material = frame_material
    def get_size(self):
        return f"{self.size} cm"
    def get_perimeter(self):
        return f"Perimeter: {round(self.size*3.1415)}cm"
    def get_km_per_rotation(self):
        #rotations it takes per kilometers
        return f"It takes about {round(100000/(self.size*3.1415))} rotations to cover 1km."

    pass
class Bicycle:
    def __init__(self,size,frame_material):
        self.obj1 = Wheel(size,frame_material)
    def ride(self):
        return f"Bicycle Wheel Size: {self.obj1.size}\nBicycle Wheel Material: {self.obj1.material}"
        #print wheel size & frame material

test = Wheel(26,'aluminum')
print(Bicycle().ride(26,'aluminum'))
#Create an object with a wheel size 26 and frame aluminum
#How many kilometer per rotation do you get on that wheel?