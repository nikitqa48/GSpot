


class Reciever:

    def __init__(self, pubsub, websocket):
        self.websocket = websocket
        self.pubsub = pubsub
        self.flag = True

    async def recieve(self):
        while self.flag:
            try:
                message = await self.pubsub.get_message()
                if message is not None:
                    if type(message['data']) is not int:
                        await self.websocket.send_text(message['data'])
            except:
                self.flag = False