from fastapi import APIRouter
from app.models.wifi_model import WifiInput
from app.services.wifi_services import analyze_wifi

router = APIRouter()

@router.post("/predict")
def predict_wifi(data: WifiInput):
    return analyze_wifi(data)