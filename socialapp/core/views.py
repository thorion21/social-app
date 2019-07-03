from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comment

# Create your views here.


def index(request):
    return HttpResponse('I think it works...')


def posts_page(request):
    posts = Post.objects.all().values('text', 'id')
    comments = Comment.objects.all().values('text', 'post')

    post_entries = {}
    for p in posts:
        post_entries[p['id']] = { 'post_text': p['text'], 'comments': []}

    for comment in comments:
        post_entries[comment['post']]['comments'].append(comment['text'])

    html_string = ''
    for entry in post_entries:
        html_string += '<h2>' + post_entries[entry]['post_text'] + '</h2><ul>'

        for comment in post_entries[entry]['comments']:
            html_string += '<li>' + comment + '</li>'

        html_string += '</ul><br>'

    return HttpResponse(html_string)
