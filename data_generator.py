import pandas as pd
import numpy as np

# ----------------------------------------------------------
# Define the player base with real South African PSL players
# ----------------------------------------------------------
players: list[dict[str, object]] = [
    {"Player Name": "Themba Zwane", "Team": "Mamelodi Sundowns", "Position": "Midfielder"},
    {"Player Name": "Peter Shalulile", "Team": "Mamelodi Sundowns", "Position": "Forward"},
    {"Player Name": "Lucas Ribeiro", "Team": "Mamelodi Sundowns", "Position": "Forward"},
    {"Player Name": "Teboho Mokoena", "Team": "Mamelodi Sundowns", "Position": "Midfielder"},
    {"Player Name": "Aubrey Modiba", "Team": "Mamelodi Sundowns", "Position": "Defender"},
    {"Player Name": "Ashley Du Preez", "Team": "Kaizer Chiefs", "Position": "Forward"},
    {"Player Name": "Keagan Dolly", "Team": "Kaizer Chiefs", "Position": "Midfielder"},
    {"Player Name": "Yusuf Maart", "Team": "Kaizer Chiefs", "Position": "Midfielder"},
    {"Player Name": "Edmilson Dove", "Team": "Kaizer Chiefs", "Position": "Defender"},
    {"Player Name": "Mduduzi Shabalala", "Team": "Kaizer Chiefs", "Position": "Forward"},
    {"Player Name": "Monnapule Saleng", "Team": "Orlando Pirates", "Position": "Winger"},
    {"Player Name": "Deon Hotto", "Team": "Orlando Pirates", "Position": "Midfielder"},
    {"Player Name": "Zakhele Lepasa", "Team": "Orlando Pirates", "Position": "Forward"},
    {"Player Name": "Miguel Timm", "Team": "Orlando Pirates", "Position": "Midfielder"},
    {"Player Name": "Tapelo Xoki", "Team": "Orlando Pirates", "Position": "Defender"},
    {"Player Name": "Khanyisa Mayo", "Team": "Cape Town City FC", "Position": "Forward"},
    {"Player Name": "Thabo Nodada", "Team": "Cape Town City FC", "Position": "Midfielder"},
    {"Player Name": "Marc van Heerden", "Team": "Cape Town City FC", "Position": "Defender"},
    {"Player Name": "Iqraam Rayners", "Team": "Stellenbosch FC", "Position": "Forward"},
    {"Player Name": "Jayden Adams", "Team": "Stellenbosch FC", "Position": "Midfielder"},
    {"Player Name": "Devin Titus", "Team": "Stellenbosch FC", "Position": "Winger"},
    {"Player Name": "Siphesihle Ndlovu", "Team": "SuperSport United", "Position": "Midfielder"},
    {"Player Name": "Bradley Grobler", "Team": "SuperSport United", "Position": "Forward"},
    {"Player Name": "Thapelo Maseko", "Team": "SuperSport United", "Position": "Winger"},
    {"Player Name": "Sibusiso Vilakazi", "Team": "Sekhukhune United", "Position": "Midfielder"},
    {"Player Name": "Elias Mokwana", "Team": "Sekhukhune United", "Position": "Forward"},
    {"Player Name": "Lantshene Phalane", "Team": "Royal AM", "Position": "Midfielder"},
    {"Player Name": "Andre de Jong", "Team": "Royal AM", "Position": "Forward"},
    {"Player Name": "Sphesihle Maduna", "Team": "AmaZulu FC", "Position": "Midfielder"},
    {"Player Name": "Bonginkosi Ntuli", "Team": "AmaZulu FC", "Position": "Forward"}
]

# ----------------------------------------------------------
# Extra data pools (for randomization)
# ----------------------------------------------------------
cars = [
    "BMW X3", "Mercedes-Benz A200", "Volkswagen Polo GTI", "Toyota Hilux",
    "Audi A3", "Ford Ranger", "Hyundai Tucson", "Nissan Navara",
    "Kia Sportage", "Mazda CX-5"
]

cities = [
    "Johannesburg", "Pretoria", "Durban", "Cape Town",
    "Bloemfontein", "Polokwane", "Port Elizabeth"
]

# ----------------------------------------------------------
# Generate realistic random personal and performance stats
# ----------------------------------------------------------
for player in players:
    player["Age"] = int(np.random.randint(22, 36))
    player["Number of Kids"] = int(np.random.randint(0, 4))
    player["Car Owned"] = str(np.random.choice(cars))
    player["City"] = str(np.random.choice(cities))
    player["Matches"] = int(np.random.randint(20, 30))
    player["Goals"] = int(np.random.randint(0, 15))
    player["Assists"] = int(np.random.randint(0, 10))
    player["Yellow Cards"] = int(np.random.randint(0, 6))
    player["Red Cards"] = int(np.random.randint(0, 2))
    player["Pass Accuracy (%)"] = int(np.random.randint(75, 95))
    player["Minutes Played"] = int(np.random.randint(1200, 2700))

# ----------------------------------------------------------
# Convert to DataFrame and save as Excel
# ----------------------------------------------------------
df = pd.DataFrame(players)
df.to_excel("south_african_soccer_dataset.xlsx", index=False)

# ----------------------------------------------------------
# Print confirmation and sample
# ----------------------------------------------------------
print("✅ Excel file 'south_african_soccer_dataset.xlsx' created successfully!")
print(df.head(10))
