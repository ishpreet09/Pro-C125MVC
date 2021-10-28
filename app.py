from flask import Flask, request, jsonify
from classifier import get_prediction

app=Flask(__name__)

@app.route('/predict-data', methods=['POST'])
def predict_data():
    image=request.files.get("alphabet")
    predicting=get_prediction(image)
    return jsonify({
        'value':predicting
    }),200

if __name__=='__main__':
    app.run(debug=True)