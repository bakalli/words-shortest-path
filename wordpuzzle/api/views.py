from django.http import HttpResponse
from django.views import View

from .word_loader import WordLoader
from .services import WordPuzzleSolverService


class WordPuzzleApi(View):
    """Implement the API here"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.word_service = WordPuzzleSolverService()

    async def get(self, request, *args, **kwargs):
        words = WordLoader.get_word_set()

        return HttpResponse("Implementation needed")


    async def post(self, request, *args, **kwargs):
        serializer = WordPuzzleSerializer(data=request.data)
        if serializer.is_valid():
            start_word = serializer.validated_data['startWord']
            end_word = serializer.validated_data['endWord']

            # Run puzzle solver
            result = async self.word_service.solve_puzzle(start_word, end_word)

            return Response({'result': result}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
