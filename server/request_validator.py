from flask import abort


class RequestValidator:

    ignoreables = ['deleted']

    def __init__(self, request):


        self.request = request
        self.validate_json()

    def validate_json(self):

        """
        lets validate that the request is json
        :return:
        """

        if not self.request.json:
            abort(400, 'Expects a json response')
            # or not 'title' in request.json:

    def validate_fields(self, model):

        """
        lets validate that the request has the required model fields
        :param model:
        :return:
        """

        for field in model.fields:
            if field not in self.request.json and field not in self.ignoreables:
                abort(422, field)
