from django.shortcuts import render
from django.http import HttpResponse


def first(request):
    return HttpResponse("It's your first view")


def index(request):
    return HttpResponse("It's an index page! For lesson 33.")


def main_article(request):
    return HttpResponse("There will be a list with articles")


def unique_article(request):
    return HttpResponse("This is a unique answer for unique value")


def article(request, article_id, name=''):
    return HttpResponse(
        "This is an article #{}. {}".format(article_id, "Name of this article is '{}'".format(
            name) if name else "This is an unnamed article")
    )


def article_sub(request, subarticle, name=''):
    return HttpResponse("This is a subarticle named {}.".format(subarticle))


def article_archive(request):
    return HttpResponse("This is an archive")


def article_users(request):
    return HttpResponse("This is a list of users")


def article_number(request, artnum):
    return HttpResponse("This is archived article number {}.".format(artnum))


def user_number(request, usernum):
    return HttpResponse("This is a page of user {}.".format(usernum))
