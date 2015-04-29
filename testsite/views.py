from django.http import HttpResponse

def hello(request, something):
	if(something == "LAL"):
		return HttpResponse("chivo??!1")
	return HttpResponse("hello world")