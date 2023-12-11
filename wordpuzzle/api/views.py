from django.http import HttpResponse
from django.views import View

from .word_loader import WordLoader


class WordPuzzleApi(View):
    """Implement the API here"""

    def get(self, request, *args, **kwargs):
        words = WordLoader.get_word_set()

        return HttpResponse("Implementation needed")
