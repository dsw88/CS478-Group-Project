
import dill as pickle
import pandas as pd
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

df = pd.read_csv('{}/model_files/data-4-7-18-full.csv'.format(dir_path))
mlp_model = None
with open('{}/model_files/mlp-model.pkl'.format(dir_path), 'rb') as modelfile:
    mlp_model = pickle.load(modelfile)

gb_model = None
with open('{}/model_files/gb-model.pkl'.format(dir_path), 'rb') as modelfile:
    gb_model = pickle.load(modelfile)

rf_model = None
with open('{}/model_files/rf-model.pkl'.format(dir_path), 'rb') as modelfile:
    rf_model = pickle.load(modelfile)

preprocessor = None
with open('{}/model_files/feature-preprocessor.pkl'.format(dir_path), 'rb') as modelfile:
    preprocessor = pickle.load(modelfile)

def predict_car(car):
    df_index = [
        "listing_id",
        "vin",
        "make",
        "model",
        "year",
        "mileage",
        "transmission",
        "exterior_color",
        "state",
        "price",
        "source" 
    ]
    df_series = [[
        "Predict", # Use to get it
        'FakeVin', # Not using VIN
        car['make'],
        car['model'],
        int(car['year']),
        float(car['mileage']),
        car['transmission'],
        'FakeColor', # Not using color
        car['state'],
        0, # We're trying to predict price
        'FakeSource' # Not using source
    ]]
    new_df = pd.DataFrame(df_series, columns=df_index)
    merged_df = new_df.append(df, ignore_index=True)
    features_encoded, labels = preprocessor.get_features_encoded(merged_df, pd)
    mlp_predicted = mlp_model.predict(features_encoded.head(1))[0]
    gb_predicted = gb_model.predict(features_encoded.head(1))[0]
    rf_predicted = rf_model.predict(features_encoded.head(1))[0]
    mean_predicted = (mlp_predicted + gb_predicted + rf_predicted) / 3.0
    return {
        "mlp": mlp_predicted,
        "gb": gb_predicted,
        "rf": rf_predicted,
        "mean": mean_predicted
    }