from rest_framework import serializers

class WordPuzzleSerializer(serializers.Serializer):
    startWord = serializers.CharField(max_length=50)
    endWord = serializers.CharField(max_length=50)