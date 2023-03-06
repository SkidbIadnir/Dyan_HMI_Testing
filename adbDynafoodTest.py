#!/usr/bin/env python3
import time
from ppadb.client import Client

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) ==0:
    print('no device !')
    quit()

device = devices[0]
device.shell('input tap 72 2064')
time.sleep(1)
device.shell('input tap 634 2047')
time.sleep(1)
device.shell('input tap 518 1527')