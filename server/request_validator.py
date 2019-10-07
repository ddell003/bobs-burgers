from flask import abort


class RequestValidator:
    """
    This class validates user input for a given model
    It gets initiated with a request and when ready to be validated it takes in a model
    """
    # fields that dont need validation on
    __ignoreables = ['deleted']

    def __init__(self, request):


        self.request = request
        self.validate_json()

    def __repr__(self):

        return repr('Request Validator')

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
            if field not in self.request.json and field not in self.__ignoreables:
                abort(422, field)
