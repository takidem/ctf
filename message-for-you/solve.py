import base64, zlib

cookie = ".eJwlyzELwjAQhuG_cmRxcagUEbqJk6uDk3Cc5msNxlzJGaWU_ncjbi8PvLN7wkwGuM6d1GAkGZTh15d0Dhrx-ss1FlQ6rt6ge_AeiYT6KEO1X9bTgibqNdOkpaN9HOUm80GbxwbGklu2D9odS_K81QrgqSmLW77kUS59.adj8rw.oRuWzgd1aZ7B0MNOUwKhGEobJ44"
data = cookie[1:]
data  = data[:data.find('.')]
decode: bytes = base64.urlsafe_b64decode(data)
print(zlib.decompress(decode).decode())

