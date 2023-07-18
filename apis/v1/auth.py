from ninja import Router
from ninja import NinjaAPI, Form
from ninja.security import HttpBearer
from authuser.models import *
from django.contrib.auth import authenticate
from plugins.hasher import hasherGenerator,decrypter
import json
from plugins.sms_token import token_verify

router = Router(tags=['Authentication'])

@router.get('/')
def get_user(request):
    auth = request.auth
    user =  CustomUser.objects.all().filter(encoded=auth).get()
    return {
        'id':user.id,
        'username':user.username,
        'email':user.email,
        'account_type':user.account_type
    }


@router.post("/token", auth=None)  # < overriding global auth
def get_token(request, username: str = Form(...), password: str = Form(...)):
    """
    This will be used as signup request.
    """
    user = authenticate(username=username, password=password)
    if user:
        hh =  hasherGenerator()
        string_formatted = hh.get('encoded').decode('utf-8')
        hh.update({'rsa_duration':24,'encoded':string_formatted})
        CustomUser.objects.all().filter(id=user.id).update(**hh)
        print(hh)
        return {'token':hh.get('encoded')}
    else: 
        return {'token':False}
        # User is authenticated


# anochiwaalfred@gmail.com
# Alfieolli
@router.get("/verify-token/{otp}", auth=None)  # < overriding global auth
def verify_token_code(request, otp:str):
    """
    Use method to verify otp code sent via sms and email
    """
    user =  CustomUser.objects.all()
    if user.filter(token=otp).exists():
        user =  user.filter(token=otp).get()
        pinid = user.token_pin_id
        d = token_verify(pin_id=pinid, token=otp)
        if d.get('verified'):
            user.is_token_verified = True
            user.token_pin_id = ''
            user.token =''
            user.save()
        return {'message':'Verified'}
    else: 
        return {'message':'Failed'}

@router.post("/logout")
def logout(request):
    auth = request.auth
    user = CustomUser.objects.all().filter(encoded=auth)
    user.update(**{'encoded':'','key':'','message':'','rsa_duration':0})
    return {'message':'User Logged Out; You can sign in again using your username and password.'}
