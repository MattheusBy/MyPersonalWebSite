import aiohttp_jinja2


async def index(request):
    context = {}
    return aiohttp_jinja2.render_template(
        'index.html', request, context=context
    )
