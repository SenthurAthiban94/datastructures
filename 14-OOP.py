class CAR:
    def __init__(self,color="white",model="A",type="Seden"):
        self.__color = color
        self._model = model
        self._type = type
        self.fourwheeler = True
    
    @property
    def color(self):
        return self.__color
    @property
    def type(self):
        return self._type
    @property
    def model(self):
        return self._model

benz = CAR(
    color="red",
    model="A1",
    type="SUV"
)

print(benz)
print(benz.color)
print(benz.type)
print(benz.model)
print(benz.fourwheeler)
benz.__color = 'yellow'         # Private read only immutable attribute
print(benz.color)               # Immutable Attribute with property no setter will be available
print(benz.type)
print(benz.model)
benz.fourwheeler = False        # Modifiable Attribute
print(benz.fourwheeler)