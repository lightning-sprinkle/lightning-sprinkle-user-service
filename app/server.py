
import app.lnd as lnd
import app.reward as reward
from flask import Blueprint, escape

# from sprinkle import app
server = Blueprint('server', __name__)
@server.route('/request-payment/<dest>')
def pay(dest):
  amt = reward.get_current_reward()
  response = lnd.send_money(dest, amt)
  payment_hash = response.payment_hash.hex()
  return f'Payment hash: {escape(payment_hash)}'
