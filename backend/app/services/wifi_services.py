from app.services.ai_services import predict
import time

def analyze_wifi(data):
    data_dict = data.dict()
    
    start = time.time()
    trust_score, status = predict(data_dict)
    end = time.time()
    
    response_time = round((end - start) * 1000, 2)
    
    return {
        "trust_score": trust_score,
        "status": status,
        "responce_time": response_time
    }
    
    
    