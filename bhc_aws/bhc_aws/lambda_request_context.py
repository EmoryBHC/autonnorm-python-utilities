

class LambdaRequestContext:
    def __init__(self, request_context: dict):
        if request_context.get('operationName') is None:
            raise Exception("OperationName not found in requestContext")
        else:
            self.operation_name = request_context['operationName']
