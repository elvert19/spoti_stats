 Spotify Listening History Analysis

Analyze your Spotify data to reveal your most played songs, artists, platforms, time trends, and more.  
Basically what Wrapped doesn’t show you like the super nerd stuff

---

## 📂 Project Structure

```bash
spotify_cleaning/
├── analysis.ipynb         # Main notebook for analysis
├── analysis.py            # Script version of the notebook
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── data/                  # Your extracted JSON files go here
│   └── Streaming_History_Audio_2021-2023_0.json
│   └── ...
└── output/
    └── cleaned_spotify_streaming_data.csv

What the Code Does
Loads and cleans your Spotify streaming history (.json)

Combines audio & video data

Adds helpful columns like:

minutes_played

hour, day_of_week

platform, content_type

Calculates:

 Most played track

 Most played artist

 Listening trends (hour/month)

 Audio vs Video breakdown

 Platform usage (Windows, iOS, Smart TV, etc.)

 Total listening time (filterable by date)

 Yearly artist trends

 Artist discovery timelines and loyalty heatmaps


Example Insights
Top 5 artists (Dec 2024–Jul 2025): Drake, Kendrick Lamar, Kanye West, The Weeknd, Westside Gunn

Most played hour: 10 PM – 12 AM

Most active months:

October 2023 — 9038 minutes

November 2023 — 8158 minutes

June 2025 — 7292 minutes

May 2025 — 7262 minutes

May 2024 — 6978 minutes

Longest listening streak: March 2024

New artists discovered: Tyla, Amaarae, Larry June

Most loyal artist: Jorja Smith (streamed every year)

⚙️ How to Use This
Clone the Repository
bash
Copy
Edit
git clone https://github.com/elvert19/spoti_stats.git
cd spoti_stats/spotify_cleaning
Get Your Spotify Data
Download your Spotify data from Spotify Takeout

Extract the .zip and move the .json files into the data/ folder

Run the Analysis
Using Jupyter Notebook:

bash
Copy
Edit
jupyter notebook analysis.ipynb
Or directly via Python script:

bash
Copy
Edit
python analysis.py
Convert notebook to script manually (optional):

bash
Copy
Edit
jupyter nbconvert --to script analysis.ipynb
📦 Requirements
Install all dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Or just:

bash
Copy
Edit
pip install pandas matplotlib seaborn
💡 Ideas for Customization
Add an upload_your_zip.py script for easier uploads

Add command-line options like start/end date filters

Auto-save graphs into the output/ folder

Export top artists/tracks into a summary.csv

Build a "Wrapped-style" summary for quick insights

🤝 Contributions  are Welcome
Feel free to tweak this repo, improve the analysis, or add your own ideas!
Highly recommended if you enjoy data s through your Spotify history.

 Note
If you're using your own Spotify data, download it from the official Spotify Privacy Portal.
It may take a few days, but it's worth it for deeper insights!





