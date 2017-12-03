from time import sleep
import boto3, json, os, uuid, logging, random, string

dynamodb = boto3.resource('dynamodb', region_name=os.environ['REGION'])
table = dynamodb.Table(os.environ['TABLE_NAME'])

def constructResponse(statusCode, responseBody):
    response = {
        "statusCode": statusCode,
        "headers": {"Content-Type": "application/json"},
        "body": responseBody
    }
    print(response)
    return response

def lambda_handler(event, context):
    print(event)
    inputBody = json.loads(event['body'])
    print(inputBody['Operation'])
    print(inputBody)
    if 'Operation' not in inputBody:
        return constructResponse(400, "Operation object not found")

    if 'ServiceName' not in inputBody:
        return constructResponse(400, "ServiceName object not found")

    if inputBody['Operation'] not in ['NEW', 'GET', 'DELETE'] :
        return constructResponse(400, "Operation "+inputBody['Operation']+" Not permitted")

    if inputBody['Operation'] == 'NEW':
        if 'ServiceURL' not in inputBody:
            return constructResponse(400, "Service URL not found")
        try:
            table.put_item(
               Item={
                    'id': inputBody['ServiceName'],
                    'url': inputBody['ServiceURL']
                }
            )
            return constructResponse(200, "Service Created")
        except Exception as e:
            return constructResponse(400, e)

    if inputBody['Operation'] == 'GET':
        try:
            response = table.get_item(
                Key={
                    'id': inputBody['ServiceName'],
                }
            )
            return constructResponse(200, "Service URL: "+response['Item']['url'])
        except Exception as e:
            return constructResponse(400, e)

    if inputBody['Operation'] == 'DELETE':
        try:
            response = table.delete_item(
                Key={
                    'id': inputBody['ServiceName'],
                }
            )
            return constructResponse(200, "Service Deleted")
        except Exception as e:
            return constructResponse(400, e)
