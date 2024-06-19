class MyClass:
    def method_1(self) -> None:
        print('method 1')

    def __method_2(self) -> None:
        print('method 2')


obj = MyClass()
obj.method_1()  # method 1
# AttributeError: 'MyClass' object has no attribute '__method_2'.
obj.__method_2()
