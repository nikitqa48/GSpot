


class WebSocketView:

    def __init__(self, request, model):
        self.action = request.action
        self.model = model
        self.user = request.user_id
        self.body = request.body

    def _validate_body(self):
        try:
            self.body = self.model.parse_obj(self.body)
        except:
            self.body = 'xz'

    def create(self):
        pass

    def update(self):
        pass

