FROM public.ecr.aws/docker/library/python:3.11.9-alpine3.19 AS MOCKER

ARG DIRECTORY_PATH=${DIRECTORY_PATH}

WORKDIR /opt/$DIRECTORY_PATH
WORKDIR /opt

#Copy file to generate mock files
COPY ./app/client/test/MockingFileGenerator.py .

#Mocked files gets generated
RUN python3 MockingFileGenerator.py

FROM mcr.microsoft.com/powershell AS FINAL
WORKDIR /opt
ARG DIRECTORY_PATH=${DIRECTORY_PATH}
ARG API_SERVICE_ADDRESS=${API_SERVICE_ADDRESS}

COPY --from=MOCKER /opt/$DIRECTORY_PATH /opt/$DIRECTORY_PATH

COPY app/client/src/SLA_Checker.ps .
#RUN pwsh ./SLA_Checker.ps -directory ${DIRECTORY_PATH} -address ${API_SERVICE_ADDRESS}
ENV DIRECTORY_PATH=${DIRECTORY_PATH}
ENV API_SERVICE_ADDRESS=${API_SERVICE_ADDRESS}
ENTRYPOINT pwsh ./SLA_Checker.ps -directory ${DIRECTORY_PATH} -address ${API_SERVICE_ADDRESS}
#ENTRYPOINT ["tail", "-f", "/dev/null"]