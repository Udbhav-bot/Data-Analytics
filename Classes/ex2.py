class dog:
    #init is used to intialize the object
    def __init__(self, breed , age, weight):
        self.breed = breed
        self.age= age
        self.weight= weight
        print('Dog object created')


panther=dog(breed='German Shephered', age=11, weight=30)
tiger=dog(breed='Golden retriver', age=8, weight=27)
blacky=dog(breed='Labrador', age=5, weight=15)

print(panther.breed)
print(tiger.breed)
print(blacky.breed)


print(panther.age)
print(type(panther))