import numpy as np
import pandas as pd
import keras.models
from sklearn.metrics import mean_squared_error, mean_absolute_error


def evaluate_model(model, test_data):

    # Prepare input data for the model
    input_data = [
        test_data['user_id'].values,
        test_data['item_id'].values,
        test_data['occupation'].values,
        test_data['age'].values,
        test_data['gender'].values,
    ] + [test_data[list(test_data)[i]] for i in range(6, 25)]

    # Make predictions using the model
    predictions = model.predict(input_data).flatten()

    # Extract true ratings from the test data
    true_ratings = test_data['rating'].values

    # Calculate evaluation metrics
    rmse = mean_squared_error(true_ratings, predictions)**0.5
    mae = mean_absolute_error(true_ratings, predictions)

    return rmse, mae


def evaluate():

    test_data = pd.read_csv('./benchmark/data/test.csv')
    model = keras.models.load_model('./models/model.keras')

    rmse, mae = evaluate_model(model, test_data)

    print(f'Root Mean Squared Error (MSE): {mse}')
    print(f'Mean Absolute Error (MAE): {mae}')
  

if __name__ == '__main__':
    evaluate()

