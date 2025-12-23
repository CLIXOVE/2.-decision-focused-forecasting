import numpy as np

def static_last_observed(yesterday_demand, buffer_units=20):
    return yesterday_demand + buffer_units

def dynamic_buffer(forecast, min_buffer=10, scale=0.2):
    return np.maximum(min_buffer, scale * forecast)

def forecast_informed_order(forecast, buffer_units):
    return forecast + buffer_units
