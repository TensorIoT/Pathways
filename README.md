# Pathways

This service provide a simple service discovery solution for microservices. There are 3 operations(NEW, GET and DELETE) in this service

## Input Format for New service
	
~~~~
{
    "Operation": "NEW",
    "ServiceName": "SAMPLEService",
    "ServiceURL": "http://www.yourservice.com"
}
	
~~~~

## Input Format for getting an existing service

	
~~~~
{
    "Operation": "GET",
    "ServiceName": "SAMPLEService"
}
	
~~~~

## Input Format for deleting an existing service
	
~~~~
{
    "Operation": "DELETE",
    "ServiceName": "SAMPLEService"
}
	
~~~~

## Update Operation

Perform Delete and Insert

