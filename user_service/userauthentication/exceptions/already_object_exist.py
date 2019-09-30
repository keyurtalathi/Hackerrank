from userauthentication.conf.error_object import ErrorObject


class AlreadyExist(Exception):
	"""Raise when something goes wrong in the request validation"""
	def __init__(self,entity="Object",errorObject=None):
		if errorObject:
			self.errorObject = errorObject
		else:
			self.errorObject = ErrorObject(errorCode=409,errorMessage=(entity + " Already Exists"))

	def __str__(self):
		return str(self.errorObject.errorMessage)