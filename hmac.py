"""

Title: A "keyed-hash message authentication code" implementation in pure python.

Author: Baris CUHADAR. E-mail: baris@neovo.org

License: This code is in Public Domain or MIT License, choose suitable one for you.

Description: This HMAC implementation is in accordance with RFC 2104 specification.
             User supplied "key" and "message" must be a Python Byte Object.

             Usage:

             h = HMAC (b"key",b"The quick brown fox jumps over the lazy dog",md5)
             h.hexdigest() => outputs 80070713463e7749b90c2dc24911e275
"""


from hashlib import md5,sha1,sha256
from zlib import crc32,adler32

class HMAC:

        def __init__(self,key,message,hash_h=md5):
                
                """ key and message must be byte object """
                
                
                self.i_key_pad = bytearray()
                self.o_key_pad = bytearray()
                self.key = key 
                self.message = message 
                self.blocksize = 64
                self.hash_h = hash_h
                self.init_flag = False


        def init_pads(self):

                """ creating inner padding and outer padding """
                
                for i in range(self.blocksize):
                        self.i_key_pad.append(0x36 ^ self.key[i])
                        self.o_key_pad.append(0x5c ^ self.key[i])


        def init_key(self):
                
                """ key regeneration """
                
                if len(self.key) > self.blocksize:
                        self.key = bytearray(md5(key).digest())
                elif len(self.key) < self.blocksize:
                        i = len(self.key)
                        while i < self.blocksize:
                                self.key += b"\x00"
                                i += 1


        def digest(self):

                if self.hash_h == adler32 or self.hash_h == crc32:
                        return self.hash_h(bytes(self.o_key_pad)+str(self.hash_h(bytes(self.i_key_pad)+self.message)).encode())
                """ returns a digest, byte object. """
                """ check if init_flag is set """
                
                if self.init_flag == False:
                        
                        self.init_key()
                        self.init_pads()

                        """ hold init_flag for good. """

                        self.init_flag = True
                
                """ Drum roll for crazy one-liners! """

                return self.hash_h(bytes(self.o_key_pad)+self.hash_h(bytes(self.i_key_pad)+self.message).digest()).digest()

        def hexdigest(self):

                if self.hash_h == adler32 or self.hash_h == crc32:
                        return hex(self.hash_h(bytes(self.o_key_pad)+str(self.hash_h(bytes(self.i_key_pad)+self.message)).encode()))[2:]
                """ returns a digest in hexadecimal. """
                """ check if init_flag is set """
                
                if self.init_flag == False:

                        """ init key and padding. """

                        self.init_key()
                        self.init_pads()

                        """ set init_flag for good. """
                        
                        self.init_flag = True
                        
                """ Roll your drums, bells and kams !.. """
                        
                return self.hash_h(bytes(self.o_key_pad)+self.hash_h(bytes(self.i_key_pad)+self.message).digest()).hexdigest()

