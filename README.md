🎵 Spotify Streaming Data Pipeline & Analysis
A data engineering and analysis project that transforms raw JSON streaming history from Spotify into structured insights. This tool provides a granular look at listening habits, surpassing the limitations of the standard annual "Spotify Wrapped."

# Project Overview
This project implements an ETL (Extract, Transform, Load) pipeline to process personal Spotify data. It parses complex nested JSON files, cleans and normalizes the data using Pandas, and generates visualizations using Matplotlib.

Key Features:

Data Parsing: Converts raw Spotify JSON exports into structured CSV format.

Data Cleaning: Handles timestamp conversion, missing values, and platform categorization.

Interactive Querying: CLI-based search tool to retrieve statistics for specific songs (Play count, First-played date).

Visualization: Generates "Loyalty Heatmaps," hourly listening trends, and platform usage breakdowns.

# File Structure
Plaintext

├── data/                   # Raw JSON and Processed CSV files
├── notebooks/
│   └── analysis.ipynb      # Jupyter Notebook for EDA and visualization
├── src/
│   └── spotify.py          # Main script for data processing and querying
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

# 📊 Insights & Visualizations
The analysis uncovers patterns not available in the standard Spotify app:

Temporal Trends: Identified peak listening hours (10 PM – 12 AM) and most active months (October/November).

Platform Analysis: Breakdown of listening time across devices (iOS vs. Desktop vs. Smart TV).

Artist Loyalty: Calculated distinct "discovery dates" for artists to track long-term fandom.

(Note: Add a screenshot of one of your graphs here, e.g., ![Listening Trends](path/to/image.png))

# Installation & Usage
Clone the repository:

Bash

git clone https://github.com/elvert19/spoti_stats.git
cd spoti_stats
Install dependencies:

Bash

pip install -r requirements.txt
Run the analysis script:

Bash

python src/spotify.py
 Technologies Used
Python 3.x

Pandas (Data manipulation & aggregation)

Matplotlib / Seaborn (Data Visualization)

Jupyter Notebooks

🤝 Contributing
Contributions are welcome! If you have ideas for new metrics or clearer visualizations, feel free to open a pull request.
