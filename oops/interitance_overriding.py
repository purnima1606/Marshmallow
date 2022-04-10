class PositivePoint:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __setattr__(self, value):
        if value < 500:
            raise ValueError("cannot set negative value: ")
        super()
