Python module for Email Center Pro
==============

ECP ( as it shall be known henceforth ) is a team-centric email service provided by Palo Alto Software. They provide some sparse code exmaples, but lack an offical module. This project seeks to fill that void with a Pythonic means of interacting with their service. Their API is considered beta presently, but they have done a fine job in documenting it.


Example
==============
```python
from emailcenterpro import ecp_connect

ecp = ecp_connect('YOUR_KEY', 'YOUR_SECRET', 'YOUR_URL')
print ecp.folder.list()
```


