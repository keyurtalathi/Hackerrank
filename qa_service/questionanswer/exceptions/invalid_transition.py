from questionanswer.conf.error_object import ErrorObject
class InvalidTransition(Exception):
	def __init__(self,entity="Object",from_state="",to_state=""):
		error_object = ErrorObject()
		error_object.errorCode = 400
		error_object.errorMessage = "Transition not allowed for "+entity
		if from_state and to_state:
			error_object.errorMessage = error_object.errorMessage + " from "+from_state+" to "+to_state
		self.errorObject = error_object

	def __str__(self):
		return str(self.errorObject.errorMessage)