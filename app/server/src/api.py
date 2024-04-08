from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/error_folder', methods=['POST'])
def process_sla_error():
    data = request.json

    # Check if the 'sla_error' key exists in the JSON data
    if 'sla_error' in data:
        sla_errors = data['sla_error']

        # Iterate over each item in the 'sla_error' list
        for sla_error in sla_errors:
            folder = sla_error.get('folder')
            sla = sla_error.get('sla')
            files = sla_error.get('files')

            print(f"Folder: {folder}, SLA: {sla}")
            for file_info in files:
                filename = file_info.get('filename')
                creation_date = file_info.get('creationDate')
                print(f"File Name: {filename}, Creation Date: {creation_date}")
        
        return jsonify({"message": "Data processed successfully."}), 200
    else:
        return jsonify({"error": "No 'sla_error' key found in the request."}), 400

if __name__ == '__main__':
    app.run(debug=True)
