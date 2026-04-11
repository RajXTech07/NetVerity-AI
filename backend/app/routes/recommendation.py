from fastapi import APIRouter
from app.models.wifi_model import WifiInput
from app.utils.score_calculator import calculate_score

router = APIRouter()

@router.post("/recommend")
def get_recommendation(data: WifiInput):
    data_dict = data.dict()
    score = calculate_score(data_dict)
    
    # Status logic
    if score >= 80:
        status = "Excellent Speed"
        recommendation = "Perfect for streaming, video calls, mettings and heavy workload"
        
    elif score >= 50:
        status = "Moderate Speed"
        recommendation = "Suitable for general browsing and email, but may struggle with high-demand applications and avoid heavy tasks"
        
    else:
        status = "Worst Speed"
        recommendation = "Not reliable and unsafe.\n Avoid meetings and important works."
        
    return {
        "trust_score": score,
        "status": status,
        "recommendation": recommendation
    }
    