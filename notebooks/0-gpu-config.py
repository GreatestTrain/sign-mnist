#!/bin/python

from tensorflow import config

physical_devices = config.list_physical_devices('GPU')
# logical_devices = config.list_logical_devices('GPU')

device_memory_usage = 4096 # in MB
try:
    config.set_logical_device_configuration(
        physical_devices[0],
        [
            config.LogicalDeviceConfiguration(memory_limit=device_memory_usage),
        ]
    )
except RuntimeError as re:
    print(re)
