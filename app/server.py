
import app.lnd as lnd
import app.reward as reward
import app.cert as cert
import app.dns as dns
import app.status_image as status_image
import config
from flask import Blueprint, escape, request, render_template
from urllib.parse import urlparse
from tinydb import TinyDB, Query

server = Blueprint('server', __name__)

@server.route('/request-payment')
def request_payment():
  hostname = urlparse(request.headers.get('Referer')).netloc
  dest = dns.get_lnd_pubkey(hostname)
  if not config.organization_only or cert.isOrganization(hostname):
    amt = reward.get_current_reward()
    response = lnd.send_money(dest, amt)
    payment_hash = response.payment_hash.hex()
    return f'Payment hash: {escape(payment_hash)}'
  else:
    return f'{escape(hostname)} is not an organization'

@server.route('/request-permission')
def request_permission():
  hostname = urlparse(request.headers.get('Referer')).netloc
  return render_template("request-permission.htm", hostname=hostname)
  
@server.route('/status')
def status():
  db = TinyDB('data/database.json')
  permissions = db.table('permissions')
  Publisher = Query()
  hostname = urlparse(request.headers.get('Referer')).netloc
  publisher_permission = permissions.get(Publisher.hostname == hostname)
  if publisher_permission is None:
    return status_image.generate(1)
  elif publisher_permission.get("status") == "accepted":
    return status_image.generate(2)
  elif publisher_permission.get("status") == "rejected":
    return status_image.generate(3)
  

