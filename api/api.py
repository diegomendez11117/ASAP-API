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
    return "member_id : " + format(str(uuid.uuid4()))


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
                {"message": str("VALIDATION ERROR"), "severity": "danger"}
            ),
            401,
        )
        response.headers["Content-Type"] = "application/html"
        return response


app.run()
