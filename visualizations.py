import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def plot_state_map(df):
    fig = px.choropleth(
        df,
        locations="States/UTs",
        locationmode="country names",
        color="Domestic -2019",
        hover_name="States/UTs",
        color_continuous_scale=px.colors.sequential.Plasma,
        title="Domestic Visitors by State (2019)"
    )
    fig.update_geos(fitbounds="locations", visible=False)
    return fig

def plot_travel_modes(df, country):
    country_data = df[df['Country of Nationality'] == country]
    modes = ['Air', 'Sea', 'Land']
    values = [country_data[mode].iloc[0] for mode in modes]
    fig = px.pie(names=modes, values=values, title=f"Travel Modes for {country} (2019)")
    return fig

def plot_monthly_spending(df, year=2019):
    # Define possible month column variations
    month_variations = {
        'january': ['january', 'January', 'JAN', 'Jan', 'jan'],
        'february': ['february', 'February', 'FEB', 'Feb', 'feb'],
        'march': ['march', 'March', 'MAR', 'Mar', 'mar'],
        'april': ['april', 'April', 'APR', 'Apr', 'apr'],
        'may': ['may', 'May', 'MAY', 'may'],
        'june': ['june', 'June', 'JUN', 'Jun', 'jun'],
        'july': ['july', 'July', 'JUL', 'Jul', 'jul'],
        'august': ['august', 'August', 'AUG', 'Aug', 'aug'],
        'september': ['september', 'September', 'SEP', 'Sep', 'sep'],
        'october': ['october', 'October', 'OCT', 'Oct', 'oct'],
        'november': ['november', 'November', 'NOV', 'Nov', 'nov'],
        'december': ['december', 'December', 'DEC', 'Dec', 'dec']
    }

    # Find actual month columns in the DataFrame
    available_months = []
    month_mapping = {}
    for standard_month, variants in month_variations.items():
        for variant in variants:
            if variant in df.columns:
                available_months.append(standard_month)
                month_mapping[standard_month] = variant
                break

    if not available_months:
        st.error("No month columns found in the dataset.")
        return go.Figure()

    # Filter data for the specified year
    year_data = df[df['year'] == year]
    if year_data.empty:
        st.error(f"No data available for year {year}.")
        return go.Figure()

    # Extract values for available months
    data = year_data[[month_mapping[month] for month in available_months]].iloc[0]
    fig = go.Figure(data=[
        go.Bar(
            x=available_months,
            y=data.values,
            marker_color='indianred'
        )
    ])
    fig.update_layout(
        title=f"Foreign Exchange Earnings by Month ({year})",
        xaxis_title="Month",
        yaxis_title="Earnings (USD Billion)",
        xaxis_tickangle=-45
    )
    return fig