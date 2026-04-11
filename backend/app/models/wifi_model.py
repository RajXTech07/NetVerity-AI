from pydantic import BaseModel

class WifiInput(BaseModel):
    download: float
    upload: float
    ping: float
    jitter: float
    users_connected: int
    signal_strength: float
    packet_loss: float
    time_of_day: str
    location_type: str
    