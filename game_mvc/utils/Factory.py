class Factory:
    __creations = []

    @classmethod
    def _create(cls, type, *args, **kwargs):
        object = type(*args, **kwargs)
        if object in cls.__creations:
            return cls.__creations[cls.__creations.index(object)]
        cls.__creations.append(object)
        return object