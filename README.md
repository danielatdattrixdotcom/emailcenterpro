Python module for Email Center Pro
==============

ECP ( as it shall be known henceforth ) is a team-centric email service provided by Palo Alto Software. They provide some sparse code exmaples, but lack an offical module. This project seeks to fill that void with a Pythonic means of interacting with their service. Their API is considered beta presently, but they have done a fine job in documenting it.


Example
==============
```python
from emailcenterpro.api import ecp_connect

ecp = ecp_connect('YOUR_KEY', 'YOUR_SECRET', 'YOUR_URL')

# Actions are simple and follow the API URL path
print ecp.account.stats()

# Objects return data without an action are also implemented
print ecp.account()

# Passing in parameters, all done via keyword params
print ecp.conversation.list(mailboxId='MAILBOX_GUID')

# You can pass keyword args to ecp_connect if you always want certain parameters passed, e.g. mailboxId
ecp = ecp_connect('YOUR_KEY', 'YOUR_SECRET', 'YOUR_URL', mailboxId='MAILBOX_GUID')
```


About Email Center Pro
==============

I'm in no way affiliated with Palo Alto Software, so I'll let them handle the sales pitch for ECP.

http://www.emailcenterpro.com/