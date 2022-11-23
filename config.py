import os

class Config(object):
	SECRET_KEY = os.getenv("SECRETE_KEY", "DFHDFDDJHDFDFHJDFDJH545uerh")
	