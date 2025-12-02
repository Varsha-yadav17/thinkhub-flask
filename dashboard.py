import random

def get_dashboard_data():
    return {
        "available_slots": random.randint(1, 4),
        "predicted_occupancy": f"{random.randint(50, 95)}%",
        "fault_alerts": random.choice(["No Faults", "Maintenance Required"]),
        "utilization": f"{random.randint(40, 90)}%"
    }
