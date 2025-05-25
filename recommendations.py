def recommend_destinations(preferences, state_df, travel_modes_df):
    art_form = preferences['art_form']
    season = preferences['season']
    crowd = preferences['crowd']
    travel_mode = preferences['travel_mode']

    # Art form to state mapping
    art_to_state = {
        "Tribal": ["Nagaland", "Mizoram", "Arunachal Pradesh"],
        "Mughal": ["Uttar Pradesh", "Delhi"],
        "Temple Architecture": ["Tamil Nadu", "Odisha"],
        "Dance": ["Manipur", "Odisha"],
        "Festivals": ["Nagaland", "West Bengal"]
    }

    # Filter states by crowd level
    if crowd == "Low":
        filtered_df = state_df.nsmallest(10, "Domestic -2019")
    elif crowd == "Moderate":
        filtered_df = state_df[state_df["Domestic -2019"].between(state_df["Domestic -2019"].quantile(0.25), state_df["Domestic -2019"].quantile(0.75))]
    else:
        filtered_df = state_df.nlargest(10, "Domestic -2019")

    # Filter by art form
    states = art_to_state.get(art_form, [])
    recommendations = filtered_df[filtered_df["States/UTs"].isin(states)]["States/UTs"].tolist()

    # Consider travel mode (example: prioritize air-accessible destinations)
    if travel_mode == "Air":
        recommendations = [r for r in recommendations if r in ["Uttar Pradesh", "Tamil Nadu", "Delhi"]]  # Major airports
    elif travel_mode == "Land":
        recommendations = [r for r in recommendations if r in ["Nagaland", "Mizoram"]]  # Land-accessible

    return recommendations if recommendations else ["No matching destinations found"]