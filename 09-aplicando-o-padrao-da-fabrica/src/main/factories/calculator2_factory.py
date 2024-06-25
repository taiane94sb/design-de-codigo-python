from src.calculators.calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler


def calculator2_factory():
    numpyHandler = NumpyHandler()
    calc = Calculator2(numpyHandler)
    return calc
