# python-hmac

Title: A "keyed-hash message authentication code" implementation in pure python.

License: This code is in Public Domain or MIT License choose suitable one for you.

Description: This HMAC implementation is in accordance with RFC 2104 specification.
             User supplied "key" and "message" must be a Python Byte Object.

             Usage:

             h = HMAC (b"key",b"The quick brown fox jumps over the lazy dog",md5)
             h.hexdigest() => outputs 80070713463e7749b90c2dc24911e275
