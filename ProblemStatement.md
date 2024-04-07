# Coding Test

## Power Shell

We have folders that have files in them that move through the system as they process. A set of processes will move them to an 'archive' folder after they are
 processed. Sometimes, the processes die or slow down. Each folder has a specific SLA (20 minutes to 24 hours).

### Requirements

- You need to create a powershell that will check a list of folders to see if their SLA has been tripped.
- The powershell needs to send all of the folders, and corresponding file names that have tripped to a REST endpoint.
- The request must be a JSON object that looks like:
```json
{

    "sla_error": [

        {

            "folder": string,

            "sla": int,

            "files": [{

                "filename": string,

                "creationDate": string

            }]

        }

    ]

}
```

>NOTE: You can use a fake URL service to prove this works (POST https://reqres.in/api/errorFolder to send data. It will always return a 200, but assume other errors an occur.


## AWS Design

We need to take data from the Powershell script above and ingest it into AWS. We need to process the data by saving it into a DynamoDB. We then need to do the
 following


### Requirements

- Data received from the powershell must be passed to AWS
- AWS serverless technologies are the only option for implementation 
- Must be authorized via a username/password. 
- Design the authentication mechanism 
- Data must rest inside a DynamoDB 
- We also want to be able to search it by affected date and affected folder. 
- Affected date is the more common use case
- Must have metrics on how often the application is being used and what the HTTP status has returned


> NOTE:
https://www.drawio.com/ is a great free tool for diagramming. Feel free to use this.


## Python

The python must match the AWS Design and the input from the Powershell will be the expected input into the lambda function.

### Requirements

- Must be written in python
- Must 'write' to a dynamodb
- Response must be 200 for successes, 400s for user error, and 500 for internal system issues
- Assume the lambda_handler(event, context) is your entrypoint
- Code must utilize the boto3 SDK
- Write unit tests with moto

> NOTE: This will be executed locally,
 writing unit tests using moto will let us execute locally so we can talk through scenarios