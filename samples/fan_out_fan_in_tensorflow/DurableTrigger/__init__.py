import logging

from azure.durable_functions import DurableOrchestrationClient
import azure.functions as func


def main(req: func.HttpRequest, starter: str, message):
    function_name = req.route_params.get('functionName')
    logging.info(starter)
    client = DurableOrchestrationClient(starter)
    client.start_new(function_name, None, None)
    response = func.HttpResponse(status_code=200, body=starter)
    message.set(response)
