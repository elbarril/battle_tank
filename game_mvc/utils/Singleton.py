class Singleton:
    __instances = {}

    def __new__(cls):
        if cls.__instances.get(cls) is None:
            instance = super().__new__(cls)
            cls.__instances.setdefault(cls, instance)
        return cls.__instances.get(cls)
