# from sklearn.metrics import recall_score
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor as xgbmodel
from models.utils import prepare_train_valid_test
import pandas as pd
import numpy as np
np.random.seed(0)

def train_model_calibration_xgboost(dataset, train_per=0.6, valid_per=0.2):
    dataset = dataset.to_numpy()
    X = dataset[:, 0:-1]
    Y = dataset[:, -1]
    X_train, X_valid, X_test = prepare_train_valid_test(X, train_per, valid_per)
    y_train, y_valid, y_test = prepare_train_valid_test(Y, train_per, valid_per)
    model = xgbmodel(objective='reg:squarederror')
    model.fit(X_train, y_train, eval_metric="mae", eval_set=[(X_valid, y_valid)], verbose=False)
    pickle.dump(model, open("pretrained/xgboost_calibration.dat", "wb"))


def calibrate_data_xgboost(data):
    loaded_model = pickle.load(open("pretrained/xgboost_calibration.dat", "rb"))
    data_calibration = loaded_model.predict(data)
    return data_calibration