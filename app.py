from flask import Flask, request, jsonify
import requests
import urllib.parse

app = Flask(__name__)

@api.route('/process-url', methods=['POST'])
def process_url():
    # Get the URL from the request data
    url = request.json.get('url')

    # Perform the API request
    api_key = "Delorean_O45101175305256693567225673237273452P"
    try:
        response = requests.get("https://dlr-api-w.vercel.app")
        if response.status_code == 200:
            api = response.json()["api_url"].strip()
        else:
            return jsonify({'error': 'API is offline!'})

    except Exception as e:
        return jsonify({'error': 'API is offline!'})

    headers = {
        "Authorization": "Bearer " + api_key
    }

    response = requests.get(f"{api}/api/bypass?url={urllib.parse.quote(url)}", headers=headers)
    if response.status_code == 200:
        result_json = response.json()
        bypassed_url = result_json.get("result")
        return jsonify({'bypassed_url': bypassed_url})
    else:
        return jsonify({'error': 'Failed to bypass URL!'})

if __name__ == '__main__':
    app.run(debug=True)
