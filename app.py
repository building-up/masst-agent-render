from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/forecast', methods=['POST'])
def forecast_threat():
    data = request.get_json()
    threat_type = data.get("threat_type")
    urgency = data.get("urgency")

    response = {
        "summary": f"The threat '{threat_type}' is expected to escalate based on urgency level '{urgency}'.",
        "next_steps": [
            "Escalate to operations team",
            "Deploy preventive resources",
            "Monitor for infrastructure impact"
        ]
    }

    return jsonify(response)

