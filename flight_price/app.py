import pandas as pd
import pickle
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

scaler_path = os.getenv('SCALER_PATH')
rf_path = os.getenv('RF_PATH')

# Load models once at startup
scaler_model = pickle.load(open(scaler_path, 'rb'))
rf_model = pickle.load(open(rf_path, 'rb'))

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Ensure templates directory exists and HTML is available
if not os.path.exists("templates"):
    os.makedirs("templates")
    # Write the HTML template for the form
    with open("templates/index.html", "w", encoding="utf-8") as f:
        f.write("""
<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Flight Price Prediction</title>
    <style>
        body { font-family: 'Poppins', sans-serif; background-color: #f9f9f9; margin: 0; padding: 0; }
        .container { max-width: 800px; margin: 0 auto; padding: 40px; background-color: #ffffff; border-radius: 10px; box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1); text-align: center; }
        h1 { color: #007BFF; font-size: 36px; margin-bottom: 20px; }
        form { text-align: left; }
        input[type=\"text\"], input[type=\"number\"], select { width: 100%; padding: 15px; margin: 15px 0; border: none; border-bottom: 2px solid #007BFF; font-size: 18px; background-color: transparent; color: #333; transition: border-bottom 0.3s ease; }
        input[type=\"text\"]:focus, input[type=\"number\"]:focus, select:focus { border-bottom: 2px solid #0056b3; outline: none; }
        input[type=\"submit\"] { background-color: #007BFF; color: #fff; padding: 15px 30px; border: none; border-radius: 5px; cursor: pointer; font-size: 20px; transition: background-color 0.3s ease; }
        input[type=\"submit\"]:hover { background-color: #0056b3; }
        p#prediction { margin-top: 20px; font-size: 24px; color: #007BFF; }
    </style>
</head>
<body>
    <div class=\"container\">
        <h1>Flight Price Prediction</h1>
        <form action=\"/predict\" method=\"post\">
            <b>Select a Boarding City</b><br><br>
            <select name=\"from\">
                <option value=\"Aracaju\">Aracaju</option>
                <option value=\"Brasilia\">Brasilia</option>
                <option value=\"Campo_Grande\">Campo Grande</option>
                <option value=\"Florianopolis\">Florianopolis</option>
                <option value=\"Natal\">Natal</option>
                <option value=\"Recife\">Recife</option>
                <option value=\"Rio_de_Janeiro\">Rio de Janeiro</option>
                <option value=\"Salvador\">Salvador</option>
                <option value=\"Sao_Paulo\">Sao Paulo</option>
            </select>
            <br><br><b>Select a Destination City</b><br><br>
            <select name=\"Destination\">
                <option value=\"Aracaju\">Aracaju</option>
                <option value=\"Brasilia\">Brasilia</option>
                <option value=\"Campo_Grande\">Campo Grande</option>
                <option value=\"Florianopolis\">Florianopolis</option>
                <option value=\"Natal\">Natal</option>
                <option value=\"Recife\">Recife</option>
                <option value=\"Rio_de_Janeiro\">Rio de Janeiro</option>
                <option value=\"Salvador\">Salvador</option>
                <option value=\"Sao_Paulo\">Sao Paulo</option>
            </select>
            <br><br><b>Select Flight Class</b><br><br>
            <select name=\"flightType\">
                <option value=\"economic\">Economic</option>
                <option value=\"firstClass\">First Class</option>
                <option value=\"premium\">Premium</option>
            </select>
            <br><br><b>Select Agency</b><br><br>
            <select name=\"agency\">
                <option value=\"Rainbow\">Rainbow</option>
                <option value=\"CloudFy\">CloudFy</option>
                <option value=\"FlyingDrops\">FlyingDrops</option>
            </select>
            <br><br>
            <label for=\"day\">Day:</label>
            <input type=\"number\" name=\"day\" min=\"1\" max=\"31\" placeholder=\"Travel day\" value=\"5\">
            <label for=\"week_no\">Week No:</label>
            <input type=\"number\" name=\"week_no\" min=\"1\" max=\"53\" placeholder=\"Travel Week No\" value=\"7\">
            <label for=\"week_day\">Week Day:</label>
            <input type=\"number\" name=\"week_day\" min=\"1\" max=\"7\" placeholder=\"Travel Week Day\" value=\"5\">
            <input type=\"submit\" value=\"Predict\">
        </form>
        <p id=\"prediction\"></p>
    </div>
</body>
</html>
""")

# Mount static if the directory exists
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")






def predict_price(input_data, model, scaler):
    df_input2 = pd.DataFrame([input_data])
    X = df_input2
    X = scaler.transform(X)
    y_prediction = model.predict(X)
    return y_prediction[0]


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
async def predict(
    from_: str = Form(..., alias="from"),
    Destination: str = Form(...),
    flightType: str = Form(...),
    agency: str = Form(...),
    week_no: int = Form(...),
    week_day: int = Form(...),
    day: int = Form(...),
):
    # Prepare one-hot encoded input as before
    boarding = 'from_' + from_
    boarding_city_list = [
        'from_Florianopolis (SC)',
        'from_Sao_Paulo (SP)',
        'from_Salvador (BH)',
        'from_Brasilia (DF)',
        'from_Rio_de_Janeiro (RJ)',
        'from_Campo_Grande (MS)',
        'from_Aracaju (SE)',
        'from_Natal (RN)',
        'from_Recife (PE)'
    ]
    destination = 'destination_' + Destination
    destination_city_list = [
        'destination_Florianopolis (SC)',
        'destination_Sao_Paulo (SP)',
        'destination_Salvador (BH)',
        'destination_Brasilia (DF)',
        'destination_Rio_de_Janeiro (RJ)',
        'destination_Campo_Grande (MS)',
        'destination_Aracaju (SE)',
        'destination_Natal (RN)',
        'destination_Recife (PE)'
    ]
    selected_flight_class = 'flightType_' + flightType
    class_list = ['flightType_economic', 'flightType_firstClass', 'flightType_premium']
    selected_agency = 'agency_' + agency
    agency_list = ['agency_Rainbow', 'agency_CloudFy', 'agency_FlyingDrops']
    travel_dict = dict()
    for city in boarding_city_list:
        travel_dict[city] = 1 if city[:-5] == boarding else 0
    for city in destination_city_list:
        travel_dict[city] = 1 if city[:-5] == destination else 0
    for flight_class in class_list:
        travel_dict[flight_class] = 1 if flight_class == selected_flight_class else 0
    for ag in agency_list:
        travel_dict[ag] = 1 if ag == selected_agency else 0
    travel_dict['week_no'] = week_no
    travel_dict['week_day'] = week_day
    travel_dict['day'] = day
    try:
        predicted_price = round(predict_price(travel_dict, rf_model, scaler_model), 2)
        return JSONResponse({"prediction": str(predicted_price)})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=1112)
