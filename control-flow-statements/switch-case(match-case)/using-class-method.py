class Switch:
    @staticmethod
    def case_1():
        return "One"
    @staticmethod
    def case_2():
        return "Two"
    @staticmethod
    def case_3():
        return "Three"
    @staticmethod
    def default():
        return "Unknown"
    def switch(self, value):
        return getattr(self, f"case_{value}", self.default)()
obj = Switch()
print(obj.switch(2))