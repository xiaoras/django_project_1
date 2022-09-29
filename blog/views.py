from django.shortcuts import render
#from django.http import HttpResponse


posts = [
	{
		'author': 'AndreaD',
		'title': 'Blog Post 1',
		'content': 'Content 1',
		'date_posted': 'August 27, 2022'
	},
	{
		'author': 'JaneD',
		'title': 'Blog Post 2',
		'content': 'Content 2',
		'date_posted': 'August 28, 2022'
	},
]


def home(request):

	context = {
		'posts': posts
	}

	return render(request, 'blog/home.html', context)

def about(request):

	context = {
		'title': 'About'
	}

	return render(request, 'blog/about.html', context)
