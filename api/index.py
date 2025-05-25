# api/index.py

import json

def handler(request, response):
    # Enable CORS
    response.headers["Access-Control-Allow-Origin"] = "*"

    # Get query parameters
    names = request.query.getlist("name")  # supports ?name=X&name=Y

    # Hardcoded marks data
    marks_data = {
        "X": 10,
        "Y": 20,
        "Z": 30
    }

    # Lookup marks
    marks = [marks_data.get(name, 0) for name in names]

    return response.json({
        "marks": marks
    })
