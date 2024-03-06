from django.shortcuts import render

posts = [
  {
    'author': 'antony',
    'title': 'blog post 1',
    'content': 'first post',
    'date_posted': 'August 27, 2018'
  },
  {
    'author': 'juma',
    'title': 'blog post 2',
    'content': 'second post',
    'date_posted': 'August 28, 2018'
  }
]

def home(request):
  context = {
    'posts': posts
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})

# Create your views here.
