def handler(event,context):
  
    sla_error = event['sla_error']
    print(sla_error)

    for entry in sla_error:
        print(entry['folder'])
        folder = entry['folder']
        sla = entry['sla']
        files = entry['files']  
        print( entry['files'])
        print(f"Folder: {folder}, SLA: {sla}")
        for entry_files in files:           
            filename = entry_files['filename']
            creation_date = entry_files['creationDate']
            print(f"File Name: {filename}, Creation Date: {creation_date}")
    
    return {"statusCode":200,
            "body":"Data processed successfully."}