Cultural Odyssey India



Cultural Odyssey India is an interactive, data-driven web application designed to showcase India's rich cultural heritage, uncover unique cultural experiences, and promote responsible tourism. Built for a hackathon, the project leverages India Tourism Statistics datasets (2014–2021) and Snowflake’s cloud data platform to provide actionable insights through dynamic visualizations and personalized travel recommendations. The app empowers tourists to explore iconic cultural hotspots, discover underexplored destinations, and plan sustainable travel across India.

Hackathon Context

Developed for the Smart India Hackathon, this project addresses the Travel & Tourism | Heritage & Culture theme. It tackles the challenge of promoting India’s diverse cultural heritage while combating overtourism at popular sites (e.g., Taj Mahal: 7M visitors in 2019) and highlighting lesser-known regions (e.g., Mizoram: 24,360 domestic visitors in 2019). By combining data analytics with an intuitive UI, the app aligns with modern tourism trends like ecotourism and personalized travel planning.

Features





Dashboard: Visualize tourism trends, including:





Foreign Tourist Arrivals (FTAs): Peaked at 10.93M in 2019, dropped 74.9% in 2020.



Top States: Uttar Pradesh led with 535M domestic visitors in 2019.



Travel Modes: E.g., 80% air travel for Canadian visitors.



Foreign Exchange Earnings (FFE): $3.18B in Dec 2019.



Cultural Hotspots: Highlights iconic sites (e.g., Taj Mahal) and festivals (e.g., Durga Puja).



Underexplored Gems: Promotes low-traffic destinations like Mizoram and Arunachal Pradesh.



Responsible Tourism: Recommends low-crowd, off-season travel (e.g., Apr–Jun).



Personalized Recommendations: Suggests destinations based on preferences (e.g., Mughal Architecture, low crowd, air travel).

Prerequisites





Python 3.8–3.10: Download



Git: Install



Code Editor: VS Code or Notepad++



Snowflake Credentials (optional): For real-time data queries (CSV fallback available)

Installation





Clone the Repository:

git clone https://github.com/Aditya-96108/cultural_odyssey_India.git
cd cultural_odyssey_India



Set Up a Virtual Environment:

python -m venv venv
.\venv\Scripts\Activate.ps1



Install Dependencies:

pip install -r requirements.txt



Verify Datasets: Ensure the data/ folder contains:





General Data 2014-2020.csv



Top 10 State Visit.csv



Country Wise Visitors Ways.csv



Month Wise FFE Dollar.csv



India-Tourism-Statistics-statewise_2019-2020_domestic_foreign.csv



India-Tourism-Statistics-2021-monuments.csv



Configure Snowflake (Optional): Create a .env file in the root directory with:

SNOWFLAKE_USER=your_user
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_ACCOUNT=your_account
SNOWFLAKE_WAREHOUSE=your_warehouse

If credentials are unavailable, the app uses CSV fallback.

Usage





Run the App:

streamlit run app.py



Access the App:





Open http://localhost:8501 in a browser.



Navigate via the sidebar to:





Dashboard: View tourism trends and insights.



Cultural Hotspots: Explore iconic sites and festivals.



Underexplored Gems: Discover low-traffic destinations.



Responsible Tourism: Plan sustainable travel.



Personalized Recommendations: Input preferences (e.g., Art Form: Mughal, Crowd: Low) for tailored suggestions.



Test Features:





Select a country (e.g., Canada) on the Dashboard for travel mode insights.



Check FFE trends for 2019.



Submit a recommendation form to get destinations like Uttar Pradesh or Delhi.

Project Structure

cultural_odyssey_india/
├── app.py                    # Main Streamlit app
├── snowflake_connect.py      # Snowflake queries and CSV fallback
├── data_processing.py        # Data cleaning and processing
├── visualizations.py         # Plotly visualizations
├── recommendations.py        # Recommendation logic
├── static/                   # CSS and images
│   ├── css/
│   │   └── styles.css
│   └── images/
│       └── logo.png
├── data/                     # CSV datasets
│   ├── General Data 2014-2020.csv
│   ├── Top 10 State Visit.csv
│   └── ...
├── pages/                    # Multi-page app modules
│   ├── dashboard.py
│   ├── cultural_hotspots.py
│   ├── underexplored.py
│   ├── responsible_tourism.py
│   ├── recommendations.py
├── requirements.txt          # Dependencies
├── .env                      # Snowflake credentials (optional)
└── README.md

Technologies Used





Streamlit: Interactive web UI



Snowflake: Real-time data processing



Python: Core programming



Pandas: Data manipulation



Plotly: Visualizations



Snowflake Connector Python: Snowflake integration



Python-dotenv: Environment variables



NumPy: Numerical computations



CSS: Custom styling



Git: Version control

Challenges Overcome





Snowflake Errors: Fixed connection failures ('NoneType' object has no attribute 'find') with robust error handling and CSV fallback.



KeyError in Visualizations: Resolved column mismatches in Month Wise FFE Dollar.csv for the FFE chart.



Git Setup: Addressed branch mismatches (master vs. main) and push errors for GitHub integration.

Deployment

For a live demo, deploy to Streamlit Cloud:





Push to GitHub: https://github.com/Aditya-96108/cultural_odyssey_India



Create an app in Streamlit Cloud, linking to the repository.



Set app.py as the main file and add Snowflake credentials (if used).



Access the deployed app URL.

Contributing

Contributions are welcome! Please fork the repository, create a branch, and submit a pull request.

License

This project is licensed under the MIT License.

Acknowledgments





India Tourism Statistics datasets (2014–2021)



Smart India Hackathon for inspiration



Snowflake and Streamlit communities# cultural_odyssey_India
