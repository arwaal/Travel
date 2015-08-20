from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
# Create your views here.

from maim.models import WebUser, Picture, Comments
from maim.forms import CreateUser, Login, UploadImage
from django.contrib.auth.models import User






def home(request):
	context = {} 

	context['pictures'] = Picture.objects.all()

	return render_to_response('home.html', context, context_instance=RequestContext(request))




def all_images(request):
	images = Picture.objects.all()
	context = {}
	context['images'] = images
	
	return render_to_response('all_images.html', context, context_instance=RequestContext(request))




def image_upload(request):
	context={}
	form = UploadImage()
	context['form'] = form

	if request.method == 'POST':
		form = UploadImage(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			# context['valid'] = "Image has been Uploaded!"
			return HttpResponseRedirect('/all_images/')

	elif request.method == 'GET':
		context['valid'] = form.errors

	return render_to_response('image_upload.html', context, context_instance=RequestContext(request))



def user_create(request):
	context = {}
	form = CreateUser()
	context ['form'] = form

	if request.method =='POST':
		form = CreateUser(request.POST)

		if form.is_valid():
			form.save()

			# context['valid'] = " Welcome %s" % CreateUser(name)
			return HttpResponseRedirect('/home/')

		elif request.method =='GET':
			context ['valid'] = form.errors

	return render_to_response('user_create.html', context, context_instance=RequestContext(request))





def user_search(request):
	context = {}
	users = WebUser.objects.filter(name__istartswith=user)
	# user2 = WebUser.objects.filter(name__istartswith=last_name)
	
	if users is not None:
		context['users'] = users
		context['valid'] = " Results Found "
	else:
		context['valid'] = " No Match "

	return  render_to_response('user_search.html', context, context_instance=RequestContext(request))





def login(request):
	context={}
	context['form'] = Login()
	username = request.POST.get('username', None)
	password = request.POST.get('password', None)

	user = authenticate(username=username, password=password)

	if user is not None:
		if user.is_active:
			login(request, user)
			context['valid'] = "Login Successful"

			return HttpResponseRedirect('/home/')

		else:
			context['valid'] = "Invalid User"
	else:
		context['valid'] = "Please enter a User Name"

	return render_to_response('login.html',context, context_instance=RequestContext(request))


# def update(request, pk):
# 	context = {}
# 	user = WebUser.objects.get(pk=pk)
# 	form = Update()
# 	context['form'] = form
# 	if request.method == 'POST':
# 		form = UpdateForm(request.POST, request.FILES)
# 		user.




# def images_search(request):
# 	images = Picture.objects.filter(city=city)


# def logout(request):




	












