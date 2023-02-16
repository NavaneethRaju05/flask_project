from flask import Flask, render_template, request, url_for, redirect, jsonify
import pandas as pd
df = pd.read_csv("home_data.csv")

app = Flask(__name__)
app.secret_key = "testing"
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/submit', methods =["GET", "POST"])
def submit():
    if request.method == "POST":
       price = request.form.get("price")
       sqft_from = request.form.get("sqft_from")
       sqft_to = request.form.get("sqft_to")
       bedroom = request.form.get("bedroom")
       data_frame_obj = df.loc[(df['price'] <= int(price)) & (df['sqft_living'] >= int(sqft_from)) & (df['sqft_living'] <= int(sqft_to)) & (df['bedrooms'] == int(bedroom))]

       return data_frame_obj.to_json(orient='records')
    # return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)