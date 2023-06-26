from datetime import datetime
import hashlib

def GetMD5(input_string):
    # Create an instance of the MD5 hash object
    md5_hash = hashlib.md5()    
    input_bytes = input_string.encode('utf-8')
    md5_hash.update(input_bytes)
    hashed_string = md5_hash.hexdigest()
    return hashed_string

def GetToken(Key):
    today = datetime.today()
    formatted_date = today.strftime("%Y-%m-%d")
    valid_token = GetMD5(Key + formatted_date)
    return valid_token

# Tanggal hari ini : 2023-06-26
# ValidToken = MD5("MySecretCode"+"2023-06-26")