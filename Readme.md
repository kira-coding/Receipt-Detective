💰 Receipt Detective

A cashier at a boutique is tasked to verify the validity of a transaction using an RN (Reference Number). To do this, she manually creates a link using an RN and the last 8 digits of their account number.

Template Link:
https://apps.cbe.com.et:100/?id=<REFERENCE NUMBER><LAST 8 DIGITS>

Boutique's last 8 digits: 61108592
Example RN: FT24341HNN9T

Receipt Link:
https://apps.cbe.com.et:100/?id=FT24341HNN9T61108592

🥅 Goal: Given the account number of the boutique is always the same, let you take as an input the RN from a user and verify the transaction.

🐾 Steps:
- take RN as input from user
- use the RN and 8 last digits of the account number to build the receipt URL
- let your code download the PDF receipt using the URL
- load the PDF and obtain its contents as text (example here (https://t.me/WeeklyCoder/76?comment=325))
- extract useful information and do the verification

📅 Submissions: Sunday Morning, 2:00 LT

🪁 Send your submissions in the comments!

@WeeklyCoder | Week 59