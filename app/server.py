
import app.lnd_connector as lnd
from flask import Blueprint

mod = Blueprint('users', __name__, url_prefix='/users')

@mod.route('/')
def status():
  return 'Sprinkle is running'

@mod.route('/request-payment/<dest>')
def pay(dest):
  payment_hash = lnd.send_money(dest, 10).payment_hash.hex()
  return f'Payment hash: {escape(payment_hash)}'
