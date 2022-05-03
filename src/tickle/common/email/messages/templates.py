"""
********************************************************************************************

This module contains all the email message templates.

********************************************************************************************
"""


SUBJECT_TEMPLATE  = '{symbol} price alert'

_FOOTER_LINK = '''---

Create more free price movement alerts at: https://tickle.ryanrickgauer.com
'''

PRICE_ALERT_TEMPLATE = f'''Tickle price alert!

The price of {{symbol}} has {{movement}} to ${{price}}.

{_FOOTER_LINK}
'''










