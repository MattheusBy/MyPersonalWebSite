"""
This module sets view-functions for handling
user's requests and renders associate template
"""

import aiohttp_jinja2


async def index(request):
    context = {}
    return aiohttp_jinja2.render_template(
        'index.html', request, context=context
    )


async def chistolife(request):
    context = {}
    return aiohttp_jinja2.render_template(
        'chistolife.html', request, context=context
    )


async def djangomarket(request):
    context = {}
    return aiohttp_jinja2.render_template(
        'djangomarket.html', request, context=context
    )


async def mypersonalwebsite(request):
    context = {}
    return aiohttp_jinja2.render_template(
        'mypersonalwebsite.html', request, context=context
    )
