from django.http import HttpResponse
from django.shortcuts import render_to_response
from walk.models import Trip


#def search_form(request):
#	return render_to_response('search_form.html')

def search(request):
	error = False
	if 'passing' in request.GET:
		passing = request.GET['passing']
		if not passing:
			error = True
		else:
			trips = Trip.objects.filter(name__icontains=passing)
			return render_to_response('search_results.html',{'trips': trips, 'query': passing})
	return render_to_response('search_form.html', {'error': error})