from flask import Flask, jsonify, request, abort, make_response
from flask import render_template
import requests
import os

TEMPLATES_FOLDER = 'templates'
STATICS_FOLDER = 'static'
app = Flask(__name__, static_url_path='', static_folder=STATICS_FOLDER, template_folder=TEMPLATES_FOLDER)

BACKGROUND_IMAGE = "bg.jpg"


SA_TOKEN = None
SA_TOKEN_FROM_PATH = None
SA_TOKEN_PATH = '/var/run/secrets/kubernetes.io/serviceaccount/token'


color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}

APP_NAME = "APP_NAME" in os.environ and os.environ.get('APP_NAME') or "Get PODs"
BG_COLOR = "BG_COLOR" in os.environ and os.environ.get('BG_COLOR') or "blue"


#    return {"status": True, "message": "Success!"}


@app.route('/test', methods=['POST'])
def test():
    json_data = request.get_json(silent=True)

    if json_data["host"]:
        KUBE_HOST=json_data["host"]
    else:
        KUBE_HOST='https://kubernetes.default.svc/api/v1/namespaces/default/pods'

#    KUBE_HOST='https://jsonplaceholder.typicode.com/todos/1'

    SA_TOKEN = "token" in json_data and json_data["token"] or SA_TOKEN_FROM_PATH

    print("KUBE_HOST=" + str(KUBE_HOST))
    print("SA_TOKEN=" + str(SA_TOKEN))

    test_results = requests.get(KUBE_HOST, headers={'Authorization': 'Bearer ' + str(SA_TOKEN)},
                                        verify=False)

    print("R " + str(test_results.json()));


    if test_results.content:
        return (test_results.content, test_results.status_code, test_results.headers.items())
    else:
        return abort(make_response(test_results, 400))


@app.route('/')
def main():
    try:
        return render_template('index.html', theme=BG_COLOR, background_image=BACKGROUND_IMAGE, app_name=APP_NAME, backgroundcolor=color_codes[BG_COLOR])
    except Exception as ex:
        print(str(ex))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)