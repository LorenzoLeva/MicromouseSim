
class ErrorRaiser:
    @staticmethod
    def getNameText(name=""):
        if name is not "":
            return " for " + name
        else:
            return ""

    @staticmethod
    def raiseIsNotTuple(tup, name=""):
        name = ErrorRaiser.getNameText(name)

        def raiseError():
            raise TypeError(f'Only Cell or tuple are allowed. Received{name}: {type(tup)} of {tup}')

        if type(tup) is not tuple:
            raiseError()

        if len(tup) is not 2 or type(tup[0]) is not int or type(tup[1]) is not int:
            raiseError()
        
        return tup

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