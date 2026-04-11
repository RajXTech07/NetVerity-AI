def calculate_score(data):
    download = data["download"]
    upload = data["upload"]
    ping = data["ping"]
    jitter = data["jitter"]
    packet_loss = data["packet_loss"]
    users = data["users_connected"]
    
    # Normalize the values
    score = (
        download * 0.35 +
        upload * 0.15 +
        (100 - ping) * 0.2 +
        (100 - jitter) * 0.1 +
        (100 - packet_loss * 10) * 0.1 +
        (100 - users * 0.1) * 0.1)
    
    # Score between 0-100
    score = max(0, min(100, score))
    return int(score)