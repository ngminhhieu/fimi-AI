from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from models.data_calibration import calibrate_data_xgboost

from server.dms.sensor import (
    retrieve_sensor,
    retrieve_sensors,
    update_sensor,
)
from server.utils.response import (
    ErrorResponseModel,
    ResponseModel,
)
from server.models.sensor import SensorSchema

router = APIRouter()


@router.post("/calibrate_by_id/{device_id}", response_description="calibrate one device")
async def calibrate_one_device(device_id):
    sensors = await retrieve_sensor(device_id)
    updated_sensors = []
    for i in range(len(sensors)):
        if calibrate_data_xgboost(sensors[i]["PM2.5"]["raw"]) != 0:
            sensors[i]["PM2.5"]["calibrated"] = calibrate_data_xgboost(sensors[i]["PM2.5"]["raw"])
            updated_sensor = await update_sensor(sensors[i]["_id"], sensors[i])
            updated_sensors.append(updated_sensor)
    return ResponseMessage("calibration by device_id updated successfully.") 


@router.post("/calibrate_all_devices", response_description="calibrate all devices")
async def calibrate_all_devices(sensor: SensorSchema = Body(...)):
    sensors = await retrieve_sensors()
    updated_sensors = []
    for i in range(len(sensors)):
        if calibrate_data_xgboost(sensors[i]["PM2.5"]["raw"]) != 0:
            sensors[i]["PM2.5"]["calibrated"] = calibrate_data_xgboost(sensors[i]["PM2.5"]["raw"])
            updated_sensor = await update_sensor(sensors[i]["_id"], sensors)
            updated_sensors.append(updated_sensor)
    return ResponseMessage("calibration for all devices updated successfully.") 