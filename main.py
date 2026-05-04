import pint
import numpy as np
from scipy import constants

def equilibrium_vapor_pressure(temperature):
    tc = temperature - constants.zero_Celsius * si.K
    return 0.61078 * si.kPa * np.exp(17.27 * tc / (tc + 237.3 * si.K))

def main():
    si = pint.UnitRegistry()

    print(f"{equilibrium_vapor_pressure(temperature= 273 * si.K)=:.2g~}")
