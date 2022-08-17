# COMMANDS to cretae virtualenvironment
virtualenvironment venv

# Activate virtual environment
venv\Scripts\Activate -- for windows
venv\bin\activate

# Setting up zip
## For windows
- Download the zip.exe file from : http://stahlworks.com/dev/index.php?tool=zipunzip and add it to the classpath

## Steps to setup the deplotment package for aws lambda

- cd lambda
- pip install -r requiremets.txt --target ./package
- cd package
- zip -r ./deployment.zip .
- cd ../
- zip -g deployment.zip src

` This will create the deployment.zip file which willl have all the requirements as well as the source code.