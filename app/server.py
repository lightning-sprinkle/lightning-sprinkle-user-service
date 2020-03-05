
import app.lnd as lnd
import app.reward as reward
import app.cert as cert
import app.dns as dns
import config
from flask import Blueprint, escape, request
from urllib.parse import urlparse

server = Blueprint('server', __name__)

@server.route('/request-payment')
def request_payment(dest):
  hostname = urlparse(request.headers.get('Referer')).netloc
  dest = dns.get_lnd_pubkey(hostname)
  if not config.organization_only or cert.isOrganization(hostname):
    amt = reward.get_current_reward()
    response = lnd.send_money(dest, amt)
    payment_hash = response.payment_hash.hex()
    return f'Payment hash: {escape(payment_hash)}'
  else:
    return f'{escape(hostname)} is not an organization'
