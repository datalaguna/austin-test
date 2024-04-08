FROM public.ecr.aws/docker/library/python:3.11.9-alpine3.19 AS MOCKER

RUN mkdir /opt/dist/queue

WORKDIR /opt

#Copy file to generate mock files
COPY ./app/client/test/MockingFileGenerator.py .
#Mocked files gets generated
RUN python3 MockingFileGenerator.py

FROM mcr.microsoft.com/powershell AS FINAL

WORKDIR /opt

COPY --from=MOCKER /opt/dist/queue /dist/queue

COPY app/client/src/SLA_Checker.ps1 .

RUN pwsh SLA_Checker.ps1