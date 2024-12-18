import requests
from pypdf import PdfReader
import re

BaseUrl = "https://apps.cbe.com.et:100/?id="
LastEightDigitNumber = "61108592"
ReferenceNumber = None


def get_pdf():
    if not ReferenceNumber:
        raise ("Reference number is not defined")
    url = BaseUrl + str(ReferenceNumber) + LastEightDigitNumber

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
    }
    result = requests.get(url, stream=True, headers=headers, verify=False)
    with open("Customer Receipt.pdf", "wb") as f:
        f.write(result.content)


def validate_pdf():
    content = PdfReader("Customer Receipt.pdf").pages[0].extract_text()
    info = {
        "Payer": extract_content("Payer", content),
        "Receiver": extract_content("Receiver", content),
        "Payment Date & Time": extract_content("Payment Date & Time", content),
        "Transferred Amount": extract_content("T ransferred Amount", content),
    }
    return info


def extract_content(field, content):
    pattern = str(field) + r"\s+(.*)"
    match = re.search(pattern, content)
    if match:
        return match.group(1)


ReferenceNumber = "FT24341HNN9T"
get_pdf()
info = validate_pdf()
for key,value in info.items():
    print(f"{key} : {value}")
