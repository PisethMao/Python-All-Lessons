class Demo:
    @staticmethod
    def public_method():
        print("Public method")
    @staticmethod
    def _protected_method():
        print("Protected method")
    @staticmethod
    def __private_function():
        print("Private function")
d = Demo()
d.public_method()
# d._protected_method()
# d.__private_method()