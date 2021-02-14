"""
Constants for Linak DPG Desk Panel Integration
"""

import logging

LOGGER = logging.getLogger(__package__)
DOMAIN = 'linak_dpg'
PLATFORMS = ['sensor']

"""
Device Info:
UUID: Generic Access Profile    (00001800-0000-1000-8000-00805f9b34fb)
UUID: Generic Attribute Profile (00001801-0000-1000-8000-00805f9b34fb)
UUID: Device Information        (0000180a-0000-1000-8000-00805f9b34fb)
UUID: Vendor specific           (99fa0001-338a-1024-8a49-009c0215f78a)  DPG_SERVICE_ID
UUID: Vendor specific           (99fa0010-338a-1024-8a49-009c0215f78a)
UUID: Vendor specific           (99fa0020-338a-1024-8a49-009c0215f78a)  HEIGHT_SERVICE_ID
UUID: Vendor specific           (99fa0030-338a-1024-8a49-009c0215f78a)
"""

DPG_SERVICE_ID = '99fa0001-338a-1024-8a49-009c0215f78a'
DPG_CHAR_ID = '99fa0002-338a-1024-8a49-009c0215f78a'

HEIGHT_SERVICE_ID = '99fa0020-338a-1024-8a49-009c0215f78a'
HEIGHT_CHAR_ID = '99fa0021-338a-1024-8a49-009c0215f78a'

SERVICE_MOVE_UP = '4700'
SERVICE_MOVE_DOWN = '4600'
SERVICE_STOP = 'FF00'