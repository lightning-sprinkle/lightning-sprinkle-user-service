# Lightning-sprinkle-service

This python project handles the communication between the publisher and the lightning daemon. This happens by opening an arbitrary port on the users' computer, which can be used by publishers to request a payment.

# FAQ

#### This service makes it possible to request money from my wallet and get it immediately. Can a publisher steal my complete balance?

There are a couple of security measures in place, depending on the mode the application runs.
1. Strict: Every publisher needs to ask permission once to request money (whitelist)
2. Organization: Every publisher with an OV or EV certificate can request money. 
3. Any: Any publisher can request money, but not the ones on the blacklist.

Paymetns are throttled to a certain amount per hour, which makes it also for trusted publisher impossible to empty your wallet.
