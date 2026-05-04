import pint
import numpy as np
from scipy import constants

si = pint.UnitRegistry()


def equilibrium_vapor_pressure(T):
    TC = T - constants.zero_Celsius * si.K
    return 0.61078 * si.kPa * np.exp(17.27 * TC / (TC + 237.3 * si.K))


print(f"{equilibrium_vapor_pressure(T= 273 * si.K)=:.2g~}")
