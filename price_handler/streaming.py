from __future__ import print_function

from decimal import Decimal, getcontext, ROUND_HALF_DOWN
import os, os.path

import logging
import json

import requests

from qstrader.event.event import TickEvent
from qstrader.price_handler.price_handler import PriceHandler


class TSStreamingPriceHandler(PriceHandler):
    """
    TSStreamingPriceHandler is designed to stream live ticks
    through the TradeStation WebAPI.

    """
