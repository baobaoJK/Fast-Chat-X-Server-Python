class Result:
    def __init__(self):
        self.status = 0
        self.code = 0
        self.message = ''
        self.data = None

    def set_status(self, status):
        self.status = status

    def set_code(self, code):
        self.code = code

    def set_message(self, message):
        self.message = message

    def set_data(self, data):
        self.data = data

    def to_dict(self):
        data = {
            'status': self.status,
            'code': self.code,
            'message': self.message
        }
        if self.data is not None:
            data['data'] = self.data

        return data
