from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
	{
		'author': 'Corey Shafer',
		'title': 'Blog one',
		'date_posted': 'Aug.12.18',
	},
	{
		'author': 'John Doe',
		'title': 'Blog two',
		'date_posted': 'Feb.12.20',
	},
]

def home(request):

	context = {
		'posts': posts
	}

	return render(request, "blog/home.html", context)

def about(request):
	return render(request, 'blog/about.html')
