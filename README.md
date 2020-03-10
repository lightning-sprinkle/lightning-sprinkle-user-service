# Lightning-sprinkle-service

This python project handles the communication between the publisher and the lightning daemon. This happens by opening an arbitrary port on the users' computer, which can be used by publishers to request a payment.

# FAQ

#### This service makes it possible to request money from my wallet and get it immediately. Can a publisher steal my complete balance?

There are a couple of security measures taken in place, depending on the mode the application runs in.
1. Strict: Every publisher needs to ask permission once to request money (whitelist)
2. Organization: Every publisher with an OV or EV certificate can request money. 
3. Any: Any publisher can request money, but not the ones on the blacklist.

Paymetns are throttled to a certain amount per hour, which makes it also for trusted publisher impossible to empty your wallet.

#### Why is it called Lightning Sprinkle?
The system works on the lightning protocol and gives the user the ability to leave small amounts of money in the places they have been. Just like the story of Hansel und Gretel, where they sprinkle crumbs along their path. 

Not to mention, I am dutch, so I like [hagelslag (sprinkles)](https://en.wikipedia.org/wiki/Sprinkles#History).

#### Why is this any different from the BAT-token/Brave browser?
- ICO worth of 24 million USD
- Different browser needed
- You need to be a "verified content creator", which makes it not decentral
- Tries to serve ads anyway
- You need to connect to your Uphold account to receive contributions from Brave Rewards.




