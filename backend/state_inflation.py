def get_state_inflation():
    states = [
        "Lagos", "Abuja", "Rivers", "Kano",
        "Oyo", "Ogun", "Kaduna", "Anambra"
    ]

    base = 28.5  # Nigeria CPI baseline

    return [
        {
            "state": s,
            "inflation": round(base + i * 0.4, 1)
        }
        for i, s in enumerate(states)
    ]
