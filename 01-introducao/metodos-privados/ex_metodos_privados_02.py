class MyClass:
    # método público
    def method_1(self) -> None:
        print('method 1')
        self.__method_2()

    # método privado
    def __method_2(self) -> None:
        print('method 2')


obj = MyClass()
obj.method_1()
# method 1
# method 2
