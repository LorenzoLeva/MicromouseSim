
class ErrorRaiser:
    @staticmethod
    def getNameText(name=""):
        if name is not "":
            return " for " + name
        else:
            return ""

    # ToDo rename to raiseIsNotTupleOfInt
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
    def raiseErrorOnlyStr(x, name=""):
        name = ErrorRaiser.getNameText(name)

        if type (x) is not str:
                raise TypeError(f'Only strings are allowed. Received{name}: {type (x)} = {x}')

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

    @staticmethod
    def raiseIsNotListOfStr(x, name=""):
        name = ErrorRaiser.getNameText(name)

        def raiseError():
            raise TypeError(f'Only Lists containing strings are allowed. Received{name}: {type(x)} of {x}')

        if type(x) is not list:
            raiseError()
        
        for i in x:
            if type(i) is not str:
                raiseError()
        
        return x

    @staticmethod
    def raiseNotValidKey(key, possibleKeys, name=""):
        name = ErrorRaiser.getNameText(name)

        ErrorRaiser.raiseErrorOnlyStr(key, name)
        ErrorRaiser.raiseIsNotListOfStr(possibleKeys, name)

        if key not in possibleKeys:
            raise KeyError(f'{key} not a valid option. Valid options are: {possibleKeys}')

        return key