> Author: Nestor Mora
\
> Date: April 8th 2024

# What is this project?
This is my submission for Experian, the original problem statement can be found at the file *ProblemStatement.md*, have fun cheking my code!

Overall the project structure follows the SDLC, where the developer begins writting the initial code at the *app folder* , later creating the building steps before deploying to a certain environment, therefore the *build folder*, in the end the *deploy folder* WILL contain the desired code that contains the boto3/terraform/cloudformation file that creates the required cloud resources.

An understanding is that this application follows a client-server architecure where the files, the file checker and the API lives in separate instances.

Also a current disadvantage of the the current initial layout is the monolithic project, while the final product is not monolithic, the mono-code has this disadvantage, for readability purposes it is suggested in a later version to separate this in different repositories.

That being said this current version ensures centralization and helps to establish an initial blueprint of a CI/CD

# Coding answers

## Powershell

In order to emulate the constant queue of files, the **app/test/MockingFileGenerator.py** file was generated

In order to comply with the answer, the file named **app/src/SLA_Checker.ps1 was created**



