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
    """ 
    This API enables users to interact with the WordPuzzleSolverService
    through the use of GET requests. 

    The API creates a single instance of the service, and uses it to 
    solve all puzzles (pair of startWord and endWord) which it is given.

    For GET:
    @param startWord: word from which we are starting our word search.
    @param endWord: word which we are targetting in our search. 
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.word_service = WordPuzzleSolverService()
    
    async def get(self, request, *args, **kwargs):
        # Extract parameters from the query string
        start_word = request.GET.get('startWord', '')
        end_word = request.GET.get('endWord', '')

        serializer = WordPuzzleSerializer(data={'startWord': start_word, 'endWord': end_word})
        if serializer.is_valid():
            try: 
                result = self.word_service.solve_puzzle(start_word, end_word)
                return JsonResponse({'result': result}, status=200)
            except ValueError as e:
                return JsonResponse({'exception': str(e)}, status=400)
        return JsonResponse(serializer.errors, status=400)
        
