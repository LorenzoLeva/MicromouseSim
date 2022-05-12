
class ErrorRaiser:
    @staticmethod
    def getNameText(name=""):
        if name is not "":
            return " for " + name
        else:
            return ""

    @staticmethod
    def raiseErrorOnlyInt(x, name=""):
            name = ErrorRaiser.getNameText(name)
            
            if type (x) is not int:
                raise TypeError(f'Only integers are allowed. Received{name}: {type (x)} = {x}')
    
    @staticmethod
    def raiseNoNegativeInt(x, name=""):
        name = ErrorRaiser.getNameText(name)
        
        ErrorRaiser.raiseErrorOnlyInt(x, name)

        if x < 0:
            raise IndexError(f'No negative integer are allowed. Received{name}: {type (x)} = {x}')
        
    @staticmethod
    def raiseNoZeroNegativeInt(x, name=""):
        name = ErrorRaiser.getNameText(name)
        
        ErrorRaiser.raiseErrorOnlyInt(x, name)

        if x <= 0:
            raise IndexError(f'No zero or negative integer are allowed. Received{name}: {type (x)} = {x}')