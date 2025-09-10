from flask import Flask, request, jsonify,render_template
import numpy as np
import os
import pandas as pd
from src.pipelines.predict_pline import PredictPipeline, CustomData
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)


# Route Home
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method=='GET':
        return render_template('recommend.html')
    else:
        data = CustomData(
            genre=request.form.get('genre'),
            duration=float(request.form.get('duration')),
            director=request.form.get('director'),
            year=int(request.form.get('year')),
            rating=request.form.get('rating'),
            budget=float(request.form.get('budget')),
            language=request.form.get('language'),
        )
        pred_df = data.get_data_as_dataframe()
        print("Pred DF columns:", pred_df.columns.tolist())  # Debug columns
        print(pred_df)  # Debug content
        predicting = PredictPipeline()
        results = predicting.prediction(pred_df)

        return render_template('recommend.html', recommendation_score=results[0])
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)