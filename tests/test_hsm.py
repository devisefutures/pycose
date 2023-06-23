import binascii
import cbor2
import pytest

from pycose.exceptions import CoseException, CoseIllegalAlgorithm, CoseIllegalKeyOps
from pycose.keys import OKPKey, EC2Key
from pycose.keys.cosekey import CoseKey
from pycose.keys.keyops import SignOp, VerifyOp
from pycose.messages.sign1message import Sign1Message
from pycose.headers import Algorithm, KID
from pycose.algorithms import  RsaPkcs1Sha256, RsaPkcs1Sha384, RsaPkcs1Sha512, RsaesOaepSha1, Es256, Es384, Es512

def test_sign1_encoding():

    msg = Sign1Message(
    phdr = {Algorithm: RsaPkcs1Sha256, KID: b'kid2'},
    payload = 'signed message'.encode('utf-8'))

    msg.encode(hsm=True,key_label="rsa1", user_pin="1234", lib_path="/etc/utimaco/libcs2_pkcs11.so",slot_id=3)

    msg = Sign1Message(
    phdr = {Algorithm: RsaPkcs1Sha384, KID: b'kid2'},
    payload = 'signed message'.encode('utf-8'))

    msg.encode(hsm=True,key_label="rsa1", user_pin="1234", lib_path="/etc/utimaco/libcs2_pkcs11.so",slot_id=3)

    msg = Sign1Message(
    phdr = {Algorithm: RsaPkcs1Sha512, KID: b'kid2'},
    payload = 'signed message'.encode('utf-8'))

    msg.encode(hsm=True,key_label="rsa1", user_pin="1234", lib_path="/etc/utimaco/libcs2_pkcs11.so",slot_id=3)

    msg = Sign1Message(
    phdr = {Algorithm: RsaesOaepSha1, KID: b'kid2'},
    payload = 'signed message'.encode('utf-8'))

    msg.encode(hsm=True,key_label="rsa1", user_pin="1234", lib_path="/etc/utimaco/libcs2_pkcs11.so",slot_id=3)

    msg = Sign1Message(
    phdr = {Algorithm: Es256, KID: b'kid2'},
    payload = 'signed message'.encode('utf-8'))

    msg.encode(hsm=True,key_label="brainppol2", user_pin="1234", lib_path="/etc/utimaco/libcs2_pkcs11.so",slot_id=3)

    msg = Sign1Message(
    phdr = {Algorithm: Es384, KID: b'kid2'},
    payload = 'signed message'.encode('utf-8'))

    msg.encode(hsm=True,key_label="brainppol2", user_pin="1234", lib_path="/etc/utimaco/libcs2_pkcs11.so",slot_id=3)

    msg = Sign1Message(
    phdr = {Algorithm: Es512, KID: b'kid2'},
    payload = 'signed message'.encode('utf-8'))

    msg.encode(hsm=True,key_label="brainppol2", user_pin="1234", lib_path="/etc/utimaco/libcs2_pkcs11.so",slot_id=3)
