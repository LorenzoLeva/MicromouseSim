
class ErrorRaiser:
    @staticmethod
    def raiseErrorOnlyInt(x, name=""):
            if name is not "":
                name = " for " + name
            raise TypeError(f'Only integers are allowed. Received{name}:', type (x), x)
    
    @staticmethod
    def raiseNoNegativeInt(x, name=""):
        if name is not "":
            name = " for " + name
        
        if type (x) is not int:
            ErrorRaiser.raiseErrorOnlyInt(x, name)

        if x < 0:
            raise IndexError(f'No negative integer are allowed. Received{name}: {type (x)} = {x}')
        