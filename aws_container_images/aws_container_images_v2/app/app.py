import sys
def handler(event, context):
    response = {"output":"hello"}
    # return 'Hello from AWS Lambda using Python' + sys.version + '!'
    return response