
import dill as pickle
import pandas as pd
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

df = pd.read_csv('{}/model_files/data-4-7-18-full.csv'.format(dir_path))
model = None
with open('{}/model_files/trained-model.pkl'.format(dir_path), 'rb') as modelfile:
    model = pickle.load(modelfile)

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
    predicted = model.predict(features_encoded.head(1))
    return {
        "price": predicted[0]
    }