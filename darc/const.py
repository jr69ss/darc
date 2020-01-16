# -*- coding: utf-8 -*-
"""Defined constants."""

import datetime
import json
import math
import multiprocessing
import os
import sys
import urllib

# reboot mode?
REBOOT = bool(int(os.getenv('DARC_REBOOT', '0')))

# debug mode?
DEBUG = bool(int(os.getenv('DARC_DEBUG', '0')))

# root path
ROOT = os.path.dirname(os.path.abspath(__file__))
CWD = os.path.realpath(os.curdir)

# process number
DARC_CPU = os.getenv('DARC_CPU')
if DARC_CPU is not None:
    DARC_CPU = int(DARC_CPU)

# use multiprocessing?
FLAG_MP = bool(int(os.getenv('DARC_MULTIPROCESSING', '1')))
FLAG_TH = bool(int(os.getenv('DARC_MULTITHREADING', '0')))
if FLAG_MP and FLAG_TH:
    sys.exit('cannot enable multiprocessing and multithreading at the same time')

# data storage
PATH_DB = os.path.abspath(os.getenv('PATH_DATA', 'data'))
os.makedirs(PATH_DB, exist_ok=True)

# link file mapping
PATH_LN = os.path.join(PATH_DB, 'link.csv')
PATH_QR = os.path.join(PATH_DB, '_queue_requests.txt')
PATH_QS = os.path.join(PATH_DB, '_queue_selenium.txt')

# PID file
PATH_ID = os.path.join(PATH_DB, 'darc.pid')

# extract link pattern
LINK_EX = urllib.parse.unquote(os.getenv('LINK_EX', r'.*'))

# link black list
LINK_BL = [urllib.parse.unquote(link) for link in json.loads(os.getenv('LINK_BL', '[]'))]

# Tor Socks5 proxy & control port
TOR_PORT = os.getenv('TOR_PORT', '9050')
TOR_CTRL = os.getenv('TOR_CTRL', '9051')

# Tor authentication
TOR_PASS = os.getenv('TOR_PASS')

# use stem to manage Tor?
TOR_STEM = bool(int(os.getenv('TOR_STEM', '1')))

# Tor bootstrap retry
TOR_RETRY = int(os.getenv('TOR_RETRY', '3'))

# time delta for caches in seconds
_TIME_CACHE = float(os.getenv('TIME_CACHE', '60'))
if math.isfinite(_TIME_CACHE):
    TIME_CACHE = datetime.timedelta(seconds=_TIME_CACHE)
else:
    TIME_CACHE = None
del _TIME_CACHE

# selenium wait time
_SE_WAIT = float(os.getenv('SE_WAIT', '60'))
if math.isfinite(_SE_WAIT):
    SE_WAIT = _SE_WAIT
else:
    SE_WAIT = None
del _SE_WAIT

# selenium empty page
SE_EMPTY = '<html><head></head><body></body></html>'

# link queue
MANAGER = multiprocessing.Manager()
QUEUE_REQUESTS = MANAGER.Queue()  # url
QUEUE_SELENIUM = MANAGER.Queue()  # (ts, url)
