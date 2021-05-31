def prepare_train_valid_test(data, train_size, test_size):

    valid_len = int(data.shape[0] * (1 - test_size - train_size))
    train_len = int(data.shape[0] * train_size)

    train_set = data[0:train_len]
    valid_set = data[train_len:train_len + valid_len]
    test_set = data[train_len + valid_len:]

    return train_set, valid_set, test_set


def mae(test_arr, prediction_arr):
    with np.errstate(divide='ignore', invalid='ignore'):
        error_mae = mean_absolute_error(test_arr, prediction_arr)
        return error_mae


def mse(test_arr, prediction_arr):
    with np.errstate(divide='ignore', invalid='ignore'):
        error_mse = mean_squared_error(test_arr, prediction_arr)
        return error_mse


def rmse(test_arr, prediction_arr):
    with np.errstate(divide='ignore', invalid='ignore'):
        error_rmse = np.sqrt(mean_squared_error(test_arr, prediction_arr))
        return error_rmse


def mape(test_arr, prediction_arr):
    with np.errstate(divide='ignore', invalid='ignore'):
        y_true, y_pred = np.array(test_arr), np.array(prediction_arr)
        error_mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
        return error_mape


def cal_error(test_arr, prediction_arr):
    with np.errstate(divide='ignore', invalid='ignore'):
        # cal mse
        error_mae = mae(test_arr, prediction_arr)

        # cal rmse
        error_mse = mse(test_arr, prediction_arr)
        error_rmse = rmse(test_arr, prediction_arr)

        # cal mape
        error_mape = mape(test_arr, prediction_arr)
        error_list = [error_mae, error_rmse, error_mape]
        return error_list


def save_metrics(error_list, log_dir, filename):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    error_list = error_list.tolist()
    error_list.insert(0, dt_string)
    with open(log_dir + filename + ".csv", 'a') as file:
        writer = csv.writer(file)
        writer.writerow(error_list)