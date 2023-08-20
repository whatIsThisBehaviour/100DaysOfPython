# Nesting
capitals = {
    "West Bengal": "Kolkata",
    "Uttar Pradesh": "Lucknow", 
    "Tamil Nadu": "Chennai",
    "Andhra Pradesh": "Wizag",
    "Telangana": "Hyderabad",
    "Jharkhand": "Ranchi",
    "Bihar": "Patna",
}

# Nesting a list into a dictionary

travel_log = {
    "Uttar Pradesh" : ["Kanpur", "Allahabad", "Varanasi", "Lucknow", "Sidhatrhnagar", "Rampur", "Algarh", "Ghazipur", "Mau"],
    "Madhya Pradesh" : ["Umaria", "Katni"],
}

# Nesting dictinoary inside a dictionary
travel = {
    "Uttar Pradesh" : {"Cities_Visited": ["Kanpur", "Allahabad", "Varanasi", "Lucknow", "Sidhatrhnagar", "Rampur", "Algarh", "Ghazipur", "Mau"],
                       "Times_Visited": [1, 4, 5, 1, 2, 70, 45 ,78, 1],},
}
print(travel)