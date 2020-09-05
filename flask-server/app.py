try:
    import os
    from flask import Flask, make_response, send_from_directory, render_template
    from flask_cors import CORS, cross_origin
    import helper

except Exception as e:
    print(e)

# Initializing the Flask app
app = Flask(__name__)

# Enabling `Cross Origin Resource Policy` for app
CORS(app=app, support_credentials=True)

# Setting get route
@app.route("/api/v1.0/resources/users/all", methods=["GET"])
@cross_origin(supports_credentials=True)
def get_json():
    JSON = helper.json_provider()
    return JSON

# Setting error route
@app.errorhandler(404)
def not_found(error):
    JSON = helper.error_provider()
    return make_response(JSON, 404)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')



if __name__ == "__main__":
    app.run(threaded=True, debug=True)
