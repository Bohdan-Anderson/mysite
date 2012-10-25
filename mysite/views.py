from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime, os, math

def hello(request):
	try:
		ua = request.META['HTTP_USER_AGENT']
		return HttpResponse("your browser is %s" % ua)
	except KeyError:
		ua = 'un known'
		return HttpResponse("your browser is %s"% ua)
		
def current_datetime(request):
	now = datetime.datetime.now()
	return  render_to_response('current_datetime.html', {'current_date': now})
	
def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" %(offset, dt)
	return HttpResponse(html)

	
def returnDirectories(base):
	mylist = []
	for x in os.listdir(base):
		if os.path.isdir(base+ '/' + x):
			mylist.append(((x),returnDirectories(base + '/' +x)))
		else:			
			mylist.append(((x),('')))
	return mylist
				
def site_directories(request):
	mylist = returnDirectories('.')
	return render_to_response('directories.html', {'directories': mylist})

def images(request, imagename):
	return render_to_response('image.html', {'imagename' : imagename })
	
def display_meta(request):
	values = request.META.items()
	values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>'%(k,v))
	return HttpResponse('<table>%s</table>' %'\n'.join(html))
	

###################################
#make svg stuff
###################################
def findX(incrament,incramentSize,radious):
	return(math.cos(incrament*incramentSize)*radious)
	
def findY(incrament,incramentSize,radious):
	return(math.sin(incrament*incramentSize)*radious)

def findXY(incrament,incramentSize,radious,(x,y)):
	locX = findX(incrament,incramentSize,radious)+x
	locY = findY(incrament,incramentSize,radious)+y
	return locX,locY
	
def twirl((x,y),size,scale,incraments):
	pi = math.pi
	#part of pi
	ppi = pi/incraments
	myList = []
	width = 0;
	height = 0;
	for i in range(0,incraments*2*size):
		sizeX,sizeY = findXY(i,ppi,i/scale,(0,0))
		if sizeX > width:
			width = sizeX
		if sizeY>height:
			height = sizeY
		myList.append((sizeX,sizeY))
	
	return myList,width,height
	
def makeSvg(request):
	if'size' in request.GET:
		myList = twirl((150,150),10,10,60)
		size = int(request.GET['size'])
		scale = int(request.GET['scale'])
		incraments=int(request.GET['incraments'])
		myList,width,height = twirl((150,150),size,scale,incraments)
		return render_to_response('svg_maker.html', {'data':myList, 'pastscale':scale, 'pastsize':size,'pastincraments':incraments,'height':height,'width':width},)
	else:
		myList,width,height = twirl((150,150),10,10,60)
		return render_to_response('svg_maker.html', {'data':myList, 'pastscale':10, 'pastsize':10,'pastincraments':60,'height':height,'width':width})
