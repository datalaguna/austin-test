function Invoke-ApiPostRequest {
    param(
        [string]$Url,
        [hashtable]$Body
    )

    $headers = @{
        "Content-Type" = "application/json"
    }

    $bodyJson = $Body | ConvertTo-Json

    try {
        $response = Invoke-RestMethod -Uri $Url -Method Post -Headers $headers -Body $bodyJson
        return $response
    }
    catch {
        Write-Error "Error invoking API: $_"
        return $null
    }
}

# Define the directory to search
$directory = "app/dist/queue"

# Get a list of all directories in the specified directory
$directories = Get-ChildItem -Path $directory -Directory

# Loop through each directory
foreach ($dir in $directories) {
    # Get the path to the SLA file in the current directory
    $slaFilePath = Join-Path -Path $dir.FullName -ChildPath "ToBeProcessedBefore"

    # Check if the SLA file exists
    if (Test-Path -Path $slaFilePath) {
        # Read the content of the SLA file
        $slaContent = Get-Content -Path $slaFilePath

        # Convert the content to a datetime object
        $slaDatetime = [datetime]::ParseExact($slaContent, "yyyy-MM-dd HH:mm:ss", $null)

        # Get the current datetime
        $currentDatetime = Get-Date

        # Check if the SLA datetime is in the past
        if ($slaDatetime -lt $currentDatetime) {
            $endpoint = "http://127.x.0.1/api/error_folder"
            $bodyData = @{
                "folder" = $dir.Name
                "sla" = $slaContent
                "files" = #add here the files that matches 
            }

            $response = Invoke-ApiPostRequest -Url $endpoint -Body $bodyData

            if ($response -ne $null) {
                Write-Host "API invoked successfully. Response: $response"
            } else {
                Write-Host "API invocation failed."
            }
        }
    }
}
