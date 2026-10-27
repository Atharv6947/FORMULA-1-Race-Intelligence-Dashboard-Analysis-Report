import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ---------------- DATA PREPARATION (f1.twb Schema) ----------------

teams = [
    "Red Bull Racing",
    "Mercedes",
    "Ferrari",
    "McLaren",
    "Aston Martin",
    "Alpine",
    "Williams",
    "Haas",
    "RB (AlphaTauri)",
    "Kick Sauber",
]

team_colors = {
    "Red Bull Racing": "#9c755f",
    "Mercedes": "#b07aa1",
    "Ferrari": "#e15759",
    "McLaren": "#edc948",
    "Aston Martin": "#f28e2b",
    "Alpine": "#4e79a7",
    "Williams": "#bab0ac",
    "Haas": "#76b7b2",
    "RB (AlphaTauri)": "#ff9da7",
    "Kick Sauber": "#59a14f",
}

drivers_data = [
    ("Max Verstappen", "Red Bull Racing"),
    ("Sergio Perez", "Red Bull Racing"),
    ("Lewis Hamilton", "Mercedes"),
    ("George Russell", "Mercedes"),
    ("Charles Leclerc", "Ferrari"),
    ("Carlos Sainz", "Ferrari"),
    ("Lando Norris", "McLaren"),
    ("Oscar Piastri", "McLaren"),
    ("Fernando Alonso", "Aston Martin"),
    ("Lance Stroll", "Aston Martin"),
]

driver_df = pd.DataFrame(drivers_data, columns=["Driver", "Team"])

# 1. Driver Leaderboard by Total Points
points_data = {
    "Max Verstappen": 575,
    "Sergio Perez": 285,
    "Lewis Hamilton": 234,
    "Fernando Alonso": 206,
    "Charles Leclerc": 206,
    "Lando Norris": 205,
    "Carlos Sainz": 200,
    "George Russell": 175,
    "Oscar Piastri": 97,
    "Lance Stroll": 74,
}

# 2. Driver Performance: Total Laps Led
laps_led_data = {
    "Max Verstappen": 1003,
    "Sergio Perez": 138,
    "Charles Leclerc": 94,
    "Lewis Hamilton": 82,
    "Lando Norris": 30,
    "Carlos Sainz": 28,
    "Fernando Alonso": 19,
    "George Russell": 15,
    "Oscar Piastri": 11,
    "Lance Stroll": 6,
}

# 3. Podium Achievements by Driver
podiums_data = {
    "Max Verstappen": 21,
    "Sergio Perez": 9,
    "Fernando Alonso": 8,
    "Lando Norris": 7,
    "Lewis Hamilton": 6,
    "Charles Leclerc": 6,
    "Carlos Sainz": 3,
    "George Russell": 2,
    "Oscar Piastri": 2,
    "Lance Stroll": 0,
}

# 4. GP Host Countries
host_countries = {
    "United States": 3,
    "Italy": 2,
    "Bahrain": 1,
    "Saudi Arabia": 1,
    "Australia": 1,
    "Japan": 1,
    "China": 1,
    "Miami": 1,
    "Monaco": 1,
    "Canada": 1,
    "Spain": 1,
    "Austria": 1,
    "Great Britain": 1,
    "Hungary": 1,
    "Belgium": 1,
    "Netherlands": 1,
    "Singapore": 1,
    "Mexico": 1,
    "Brazil": 1,
    "Qatar": 1,
    "Abu Dhabi": 1,
}

# 5. DNF Causes by Team
dnf_reasons = {
    "Red Bull Racing": {
        "Engine": 1,
        "Collision": 2,
        "Gearbox": 0,
        "Hydraulics": 0,
        "Brake failure": 1,
    },
    "Ferrari": {
        "Engine": 4,
        "Collision": 3,
        "Gearbox": 2,
        "Hydraulics": 1,
        "Brake failure": 1,
    },
    "Mercedes": {
        "Engine": 2,
        "Collision": 2,
        "Gearbox": 1,
        "Hydraulics": 0,
        "Brake failure": 0,
    },
    "McLaren": {
        "Engine": 2,
        "Collision": 3,
        "Gearbox": 1,
        "Hydraulics": 1,
        "Brake failure": 0,
    },
    "Alpine": {
        "Engine": 5,
        "Collision": 4,
        "Gearbox": 2,
        "Hydraulics": 2,
        "Brake failure": 1,
    },
    "Haas": {
        "Engine": 6,
        "Collision": 5,
        "Gearbox": 3,
        "Hydraulics": 2,
        "Brake failure": 2,
    },
    "Williams": {
        "Engine": 4,
        "Collision": 6,
        "Gearbox": 2,
        "Hydraulics": 1,
        "Brake failure": 1,
    },
}

# 6. Circuit DNF Heatmap Data
circuits = [
    "Bahrain",
    "Jeddah",
    "Albert Park",
    "Suzuka",
    "Shanghai",
    "Monaco",
    "Silverstone",
    "Spa",
    "Monza",
    "Interlagos",
]
seasons = [2021, 2022, 2023, 2024]
dnf_heatmap = np.array(
    [
        [2, 3, 1, 2],
        [4, 2, 3, 1],
        [5, 4, 6, 2],
        [1, 2, 1, 3],
        [3, 1, 2, 2],
        [2, 5, 3, 4],
        [3, 4, 2, 1],
        [4, 3, 5, 2],
        [2, 2, 3, 1],
        [3, 4, 2, 3],
    ]
)

# 7. Reliability Trends (Non-DNF Rate %)
reliability_df = pd.DataFrame(
    {
        "Season": [2021, 2022, 2023, 2024],
        "Max Verstappen": [90.9, 86.4, 100.0, 95.5],
        "Lewis Hamilton": [95.5, 95.5, 95.5, 90.9],
        "Charles Leclerc": [81.8, 81.8, 86.4, 95.5],
        "Lando Norris": [95.5, 90.9, 95.5, 100.0],