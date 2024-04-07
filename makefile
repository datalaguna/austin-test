powershell-question:
	python3 app/test/MockingFileGenerator.py 
	pip install -r app/src/server/requirements.txt
	python3 app/src/server/api.py
	pwsh app/src/client/SLA_Checker.ps1