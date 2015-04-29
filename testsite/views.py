from django.http import HttpResponse

def calculate(expression):
	#description
	result = expression + "lalal"
	return result

def hello(request, something):
	if(something == "LAL"):
		return HttpResponse("chivo??!1")
	if(something == ""):
		return HttpResponse("hello world")
	return HttpResponse(calculate(something))
	