import random

import requests


def send_to_the_code_phone(phone, code):
    sms = code
    login = "IsmarIsmazov"
    pwd = "4xc76m8E"
    sender = "nikita.kg"
    xml_data = f"""<?xml version="1.0" encoding="UTF-8"?>
                    <message>
                    <login>{login}</login>
                    <pwd>{pwd}</pwd>
                    <id>{sms}</id>
                    <sender>{sender}</sender>
                    <text>Code activation: {code}</text>
                    <time>20100921235957</time>
                    <phones>
                    <phone>{phone}</phone>
                    </phones>
                    <test>0</test>
                    </message>"""
    headers = {"Content-Type": "application/xml"}
    response = requests.post(
        "https://smspro.nikita.kg/api/message", data=xml_data, headers=headers
    )
    return response.status_code


def generate_verification_code():
    code = random.randint(1000, 9999)
    return str(code)