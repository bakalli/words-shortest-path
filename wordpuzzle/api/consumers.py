#api/consumers.py 
import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class WordPuzzleConsumer(AsyncWebsocketConsumer): 
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        start_word = data['startWord']
        end_word = data['endWord']

        # Perform the asynchronous operation using the puzzle solver service
        result = await WordPuzzleSolverService.solve_puzzle(start_word, end_word)

        # Send the result back to the WebSocket client
        await self.send(text_data=json.dumps({'result': result}))
