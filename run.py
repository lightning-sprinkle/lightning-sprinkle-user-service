#!/bin/python

"""
Solution to the unpaid content problem on the internet using the lightning network.
"""

from app.reward import fill_bucket
from flask import Flask, escape, request

app = Flask(__name__)

__author__ = "Daan Middendorp"
__copyright__ = "Copyright 2020, Technische Universität Berlin"
__license__ = "GPL"
__version__ = "0.0.1"

# Make sure that the bucket filler is running
fill_bucket()

# send_money('027d2456f6d4aaf27873b68b7717c8137aaa8043d687a2113b916a5016e9a880e9', 10)

