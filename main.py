import pint
import numpy as np
from scipy import constants

si = pint.UnitRegistry()


def equilibrium_vapor_pressure(temperature):
    tc = temperature - constants.zero_Celsius * si.K
    return 0.61078 * si.kPa * np.exp(17.27 * tc / (tc + 237.3 * si.K))


print(f"{equilibrium_vapor_pressure(temperature= 273 * si.K)=:.2g~}")
