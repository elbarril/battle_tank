class Factory:
    __creations = {}

    @classmethod
    def _create(cls, type, *args, **kwargs):
        type_count = cls._next_number(type)
        cls.__creations.update({type:type_count})
        return type(*args, **kwargs)
    
    @classmethod
    def _number(cls, type):
        return cls.__creations[type] if type in cls.__creations else 0
    
    @classmethod
    def _next_number(cls, type):
        return cls._number(type) + 1