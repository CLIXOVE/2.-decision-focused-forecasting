import numpy as np

def stockout_flags(actual, order_qty):
    return np.asarray(order_qty) < np.asarray(actual)

def shortage_units(actual, order_qty):
    return np.maximum(0, np.asarray(actual) - np.asarray(order_qty))

def holding_units(actual, order_qty):
    return np.maximum(0, np.asarray(order_qty) - np.asarray(actual))
