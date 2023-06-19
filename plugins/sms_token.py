import requests
import random

api_key, sender_id = (
            'TLecXOJkRRNKNQZkmeTYnpd3pjuHcRxjruSOhiBlRIArirGcoJFXM8WZhCUooV',
            'sharashell'
            )

def send_sms(phone_number='', message=''):
    try:
        url = "https://api.ng.termii.com/api/sms/send"
        payload = {
                "to": f"{phone_number}",
                "from": f"{sender_id}",
                "sms": f"{message}",
                "type": "plain",
                "channel": "generic",
                "api_key": api_key,
            }
        headers = {
        'Content-Type': 'application/json',
        }
        response = requests.request("POST", url, headers=headers, json=payload)
        return response.json()
    except:
        pass


def send_token_via_sms(recipient_phone_number):
    try:
        
        # Generate a random token
        token = '123478'
        url = "https://api.ng.termii.com/api/sms/otp/generate"
        payload = {
           "api_key": f"{api_key}",
            "pin_type": "NUMERIC",
            "phone_number": f"{recipient_phone_number}",
            "pin_attempts": 3,
            "pin_time_to_live": 60,
            "pin_length": 4
       }
        headers = {
        'Content-Type': 'application/json',
        }
        response = requests.request("POST", url, headers=headers, json=payload)
        res = response.json()
        if response.status_code == 200:
            otp = res.get('data').get('otp')
            pinid =  res.get('data').get('pin_id')
            phone_number = res.get('data').get('phone_number')
            dt = {}
            dt['token'] = otp
            dt['pinId'] = pinid
            # dt['phone_number'] = phone_number
            message = f"Your activation code : {otp}."
            send_sms(phone_number, message)
        return dt
    except Exception as e:
        return (e)
# Example usage

# send_token_via_sms(api_key, sender_id, recipient_phone_number)

def token_verify(token='', pin_id=''):
    url = "https://api.ng.termii.com/api/sms/otp/verify"
    payload = {
            "api_key": f"{api_key}",
            "pin_id": f"{pin_id}",
            "pin": f"{token}",
        }
    headers = {
    'Content-Type': 'application/json',
    }
    response = requests.request("POST", url, headers=headers, json=payload)
    return response.json()