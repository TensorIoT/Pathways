# Pathways
This service provides a simple service-discovery solution for microservices.  
There are 4 operations available to manage your library of services:
- NEW
- GET 
- DELETE
- UPDATE

## Table of Contents
* **[What is AWS Serverless Application Repository?](#what-is-aws-serverless-application-repository)**
* **[Use Cases](#use-cases)**
* **[Setup](#setup)**
* **[Usage](#use)**
* **[License](#license)**

## What is AWS Serverless Application Repository?
The [AWS Serverless Application Repository](https://aws.amazon.com/serverless/serverlessrepo/) is a collection of
serverless applications ranging from code samples and components for building web and mobile applications to back-end
processing services and complete applications. Each application is packaged with an
[AWS Serverless Application Model (SAM)](https://github.com/awslabs/serverless-application-model) template that defines
the AWS resources used. The Serverless Application Repository enables you to quickly deploy these code samples, 
components, and applications for common use cases such as web and mobile back-ends, data processing, chatbots, IoT, and
more. There is no charge to use the Serverless Application Repository - you only pay for the AWS resources used in the
applications you deploy.

## Use Cases:
1. Manage & discover the microservice endpoints for your application.
1. Provide an abstraction for addresses in your microservice architecture.

## Setup:
In your AWS console or CLI, discover your newly created API ARN resource name for your API URL prefix.
Or, assign your VPC subnet hostname or private DNS name as the endpoint.
##### CLI Use:
REST API usage:
```bash
curl -X POST -d '{...}' my_api_prefix.execute-api.{aws_region}.amazonaws.com/prod
```
##### Application Use:
As mentioned, you could use the service as a name registry to abstract your microservice endpoints.  
See documentation on generating an API SDK for programmatic access: http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-generate-sdk.html  
And an example of Javascript SDK usage: http://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-generate-sdk-javascript.html

## Usage
### Input Format for New service	
```
{
    "Operation": "NEW",
    "ServiceName": "SAMPLEService",
    "ServiceURL": "http://www.yourservice.com"
}	
```

### Input Format for getting an existing service	
```
{
    "Operation": "GET",
    "ServiceName": "SAMPLEService"
}
```

### Input Format for deleting an existing service	
```
{
    "Operation": "DELETE",
    "ServiceName": "SAMPLEService"
}
```

### Input Format for updating a service
```
{
    "Operation": "UPDATE",
    "ServiceName": "SAMPLEService",
    "ServiceURL": "http://www.yourservice.com"
}	
```

## License
This is released under the MIT license. Details can be found in the LICENSE file.