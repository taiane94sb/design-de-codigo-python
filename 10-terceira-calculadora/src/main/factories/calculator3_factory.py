from src.calculators.calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler


def calculator3_factory():
    numpyHandler = NumpyHandler()
    calc = Calculator3(numpyHandler)
    return calc
