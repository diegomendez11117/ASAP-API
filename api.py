from flask import Flask, request, jsonify, url_for, make_response, flash

import uuid

app = Flask("member_id")
app.config["DEBUG"] = True


def is_valid_uuid(value):
    try:
        uuid.UUID(value)

        return True
    except ValueError:
        return False


@app.route('/member_id', methods=['POST'])
def add():
    request_data = request.get_json()
    if ((request_data['first_name'] is None) and (request_data['last_name'] is None) and (request_data['dob'] is None) \
            and (request_data['country'] is None)):
        response = make_response(
            jsonify(
                {"Error": str("Review the parameters sent"), "severity": "danger"}
            ),
            403,
        )
        response.headers["Content-Type"] = "application/json"
        return response

    else:
        response = make_response(
            jsonify(
                {"member_id": str(uuid.uuid4())}
            ),
            200,
        )
        response.headers["Content-Type"] = "application/json"
        return response


@app.route('/member_id/validate/', methods=['GET', 'POST'])
def validate():
    member_id = request.values.get('member_id')
    if is_valid_uuid(member_id):
        response = make_response(
            jsonify(
                {"message": str("VALIDATION SUCCESS")}
            ),
            200,
        )
        response.headers["Content-Type"] = "application/json"
        return response

    else:
        response = make_response(
            jsonify(
                {"Error": str("VALIDATION ERROR"), "severity": "danger"}
            ),
            403,
        )
        response.headers["Content-Type"] = "application/html"
        return response

app.run()
