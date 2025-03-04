from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# ✅ Load trained model and label encoders
model = joblib.load("medicine_model1.joblib")
encoders = joblib.load("medicine_encoders.joblib")

@app.route("/api/medicine", methods=["POST"])
def recommend_medicine():
    try:
        data = request.json
        print("✅ Received Data:", data)

        # ✅ Handle different JSON key cases (supports both "Disease" and "disease")
        disease = data.get("Disease") or data.get("disease")
        if not disease:
            return jsonify({"error": "Missing 'Disease' field in request"}), 400
        
        # ✅ Process multiple diseases (if user enters a phrase)
        disease_list = [d.strip().lower() for d in disease.split(",")]  # Accepts comma-separated values

        valid_diseases = set(encoders["Disease"].classes_)
        encoded_diseases = []

        for d in disease_list:
            if d in valid_diseases:
                encoded_diseases.append(encoders["Disease"].transform([d])[0])
            else:
                print("✅ Available Diseases:", list(valid_diseases))  # Debugging Step
                return jsonify({"error": f"Invalid disease: {d}"}), 400

        # ✅ Convert input into the expected format for model
        encoded_input = np.array(encoded_diseases).reshape(-1, 1)  # Reshape for ML model
        medicine_predictions = model.predict(encoded_input)

        # ✅ Format response for multiple diseases
        response = {}
        for i, disease_name in enumerate(disease_list):
            response[disease_name] = {
                "Medicine Name": medicine_predictions[i][0],
                "Composition": medicine_predictions[i][1],
                "Side Effects": medicine_predictions[i][2],
                "Excellent Review %": medicine_predictions[i][3],
                "Average Review %": medicine_predictions[i][4],
                "Poor Review %": medicine_predictions[i][5],
            }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5004, debug=True)
