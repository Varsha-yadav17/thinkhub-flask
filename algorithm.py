import math

slots = {
    1: (2, 5),
    2: (8, 3),
    3: (5, 9),
    4: (1, 1)
}

def get_optimal_slot(ev_x, ev_y):
    min_dist = float("inf")
    best_slot = None

    for slot, (x, y) in slots.items():
        dist = math.sqrt((x - ev_x) ** 2 + (y - ev_y) ** 2)
        if dist < min_dist:
            min_dist = dist
            best_slot = slot

    return best_slot
