
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

    @staticmethod # TODO remove and replace with raiseIsNotType
    def raiseIsNotList(x, name=""):
        name = ErrorRaiser.getNameText(name)

        if type(x) is not list:
            raise TypeError(f'Only Lists are allowed. Received{name}: {type(x)} of {x}')
        
        return x

    @staticmethod
    def raiseIsNotType(objType, x, name= ""):
        name = ErrorRaiser.getNameText(name)

        if type(x) is not objType:
            raise TypeError(f'Only {objType} are allowed. Received{name}: {type(x)} of {x}')
        
        return x

    @staticmethod
    def raiseNotSubclass(objType, x, name=""):
        name = ErrorRaiser.getNameText(name)

        if not issubclass(type(x), objType):
            raise TypeError(f'Only subclasses of {objType} are allowed. Received{name}: {type(x)} of {x}')

        return x 

    @staticmethod
    def raiseIsNotListOfType(listType, x, name=""):
        name = ErrorRaiser.getNameText(name)
        ErrorRaiser.raiseIsNotList(x, name)

        for i in x:
            if type(i) is not listType:
                raise TypeError(f'Only Lists containing {listType} are allowed. Received{name}: {type(x)} of {x}')
        
        return x

    @staticmethod
    def raiseNotValidKey(key, possibleKeys, name=""):
        name = ErrorRaiser.getNameText(name)

        ErrorRaiser.raiseErrorOnlyStr(key, name)
        ErrorRaiser.raiseIsNotListOfType(str, possibleKeys, name)

        if key not in possibleKeys:
            raise KeyError(f'{key} not a valid option. Valid options are: {possibleKeys}')

        return key