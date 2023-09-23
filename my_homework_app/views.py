from django.shortcuts import render
import logging
# Create your views here.
from django.http import HttpResponse
logger = logging.getLogger(__name__)

def first_app(request):
    logger.info('Страница первого поекта на Django')
    html = """<!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
    </head>
    <body>
    <h1>Первый Django сайт</h1>
    </body>
    </html>"""
    return HttpResponse(html)

def about_me(request):
    logger.info('Страница знакомства')
    html = """<!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport"
                  content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Document</title>
        </head>
        <body>
        <h1>Привет, меня зовут Алексей)</h1>
        </body>
        </html>"""
    return HttpResponse(html)

