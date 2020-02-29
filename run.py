#!/bin/python

"""
Solution to the unpaid content problem on the internet using the lightning network.
"""

import lib.rpc.rpc_pb2 as ln
import lib.rpc.rpc_pb2_grpc as lnrpc
import grpc
import os
import codecs
import binascii
import hashlib
import secrets
import json

from app.reward import feed_bucket
from flask import Flask, escape, request


app = Flask(__name__)

__author__ = "Daan Middendorp"
__copyright__ = "Copyright 2020, Technische Universität Berlin"
__license__ = "GPL"
__version__ = "0.0.1"

# Due to updated ECDSA generated tls.cert we need to let gprc know that
# we need to use that cipher suite otherwise there will be a handhsake
# error when we communicate with the lnd rpc server.
os.environ["GRPC_SSL_CIPHER_SUITES"] = 'HIGH+ECDSA'

# Lnd cert is at ~/.lnd/tls.cert on Linux
cert = open(os.path.expanduser('~/.lnd/tls.cert'), 'rb').read()
creds = grpc.ssl_channel_credentials(cert)
channel = grpc.secure_channel('localhost:10009', creds)
stub = lnrpc.LightningStub(channel)

with open(os.path.expanduser('~/.lnd/data/chain/bitcoin/mainnet/admin.macaroon'), 'rb') as f:
  macaroon_bytes = f.read()
  macaroon = codecs.encode(macaroon_bytes, 'hex')


def send_money(dest, amt):
  """ 
  Transfer money using the experimental keysend method
  """
  # Generate preimage by generating cryptographic safe random bytes
  preimage = secrets.token_bytes(32) 
  payment_hash = hashlib.sha256(preimage).digest()
  # Set the preimage as a custom record in order to use the experimental keysend method
  dest_custom_records = {5482373484: preimage}

  request = ln.SendRequest(
    dest_string=dest,
    amt=amt,
    final_cltv_delta=40,
    payment_hash=payment_hash,
    dest_custom_records=dest_custom_records
  )

  return stub.SendPaymentSync(request, metadata=[('macaroon', macaroon)])

# send_money('027d2456f6d4aaf27873b68b7717c8137aaa8043d687a2113b916a5016e9a880e9', 10)

