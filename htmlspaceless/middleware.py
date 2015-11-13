from django.conf import settings
import re


patterns = [
    # Delete doubling spaces
    {
        'pattern': re.compile(r'\s+'),
        'replacement': ' ',
    },

    # Delete spaces between tags
    {
        'pattern': re.compile(r'>\s+<'),
        'replacement': '><',
    },

    # Delete newlines
    {
        'pattern': re.compile(r'>\n'),
        'replacement': '>',
    },
]


class SpacelessMiddleware(object):

    def process_response(self, request, response):
        if settings.HTMLSPACELESS_ENABLED:
            if 'text/html' in response['Content-Type']:
                for p in patterns:
                    response.content = p['pattern'].sub(p['replacement'], response.content)
        return response
