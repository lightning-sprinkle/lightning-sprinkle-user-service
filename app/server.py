
import app.lnd as lnd
from flask import Blueprint, escape

# from sprinkle import app
server = Blueprint('server', __name__)
@server.route('/request-payment/<dest>')
def pay(dest):
  payment_hash = lnd.send_money(dest, 10).payment_hash.hex()
  return f'Payment hash: {escape(payment_hash)}'
