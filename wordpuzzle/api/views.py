from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from .word_loader import WordLoader
from .services import WordPuzzleSolverService
from .serializers import WordPuzzleSerializer


class WordPuzzleApi(View):
    """Implement the API here"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.word_service = WordPuzzleSolverService()
    
    async def get(self, request, *args, **kwargs):
        # Extract parameters from the query string
        start_word = request.GET.get('startWord', '')
        end_word = request.GET.get('endWord', '')

        serializer = WordPuzzleSerializer(data={'startWord': start_word, 'endWord': end_word})
        if serializer.is_valid():
            result = self.word_service.solve_puzzle(start_word, end_word)
            # endpoint should be returning the result in JSON format, might need to use json.dump 
            return JsonResponse({'result': result}, status=200)
        return JsonResponse(serializer.errors, status=400)
        
