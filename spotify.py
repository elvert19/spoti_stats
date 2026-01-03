import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

graph_folder = "output/graphs"
if not os.path.exists(graph_folder):
    os.makedirs(graph_folder)

plot_counter = 1

def save_and_close():
    global plot_counter
    filename = f"{graph_folder}/graph_{plot_counter}.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Graph saved: {filename}")
    plt.close()
    plot_counter += 1

plt.show = save_and_close 
sns.set(style="whitegrid")

print("Script Starting...")

subfolder = "spotify_data/Spotify Extended Streaming History"
audio_files = [
    "Streaming_History_Audio_2021-2023_0.json",
    "Streaming_History_Audio_2023-2024_1.json",
    "Streaming_History_Audio_2024-2025_2.json"
]

print("Loading Data...")
audio_data = []

if not os.path.exists(subfolder):
    print(f"ERROR: Could not find folder '{subfolder}'.")
    exit()

for file in audio_files:
    file_path = os.path.join(subfolder, file)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            audio_data.extend(json.load(f))

audio_df = pd.DataFrame(audio_data)

video_file = os.path.join(subfolder, "Streaming_History_Video_2023-2025.json")
if os.path.exists(video_file):
    with open(video_file, 'r', encoding='utf-8') as f:
        video_df = pd.DataFrame(json.load(f))
else:
    video_df = pd.DataFrame(columns=audio_df.columns)

print("Cleaning Data...")

def clean_df(df, type_label):
    if df.empty: return df
    df = df.copy()
    df["timestamp"] = pd.to_datetime(df["ts"], errors='coerce')
    df["minutes_played"] = df["ms_played"] / 60000
    df = df.dropna(subset=["timestamp"])
    df = df[df["minutes_played"] >= 0.5] 
    df["content_type"] = type_label
    return df

audio_clean = clean_df(audio_df, "audio")
video_clean = clean_df(video_df, "video")
combined_df = pd.concat([audio_clean, video_clean], ignore_index=True)

combined_df["date"] = combined_df["timestamp"].dt.date
combined_df["year"] = combined_df["timestamp"].dt.year
combined_df["month_year"] = combined_df["timestamp"].dt.to_period("M")
combined_df["hour"] = combined_df["timestamp"].dt.hour
combined_df["day_of_week"] = combined_df["timestamp"].dt.day_name()

print("Data Ready. Generating Graphs...")

print("... 1. Top 100 Tracks")
most_played_tracks = combined_df.groupby("master_metadata_track_name")["minutes_played"].sum().nlargest(100)
plt.figure(figsize=(15, 25))
sns.barplot(x=most_played_tracks.values, y=most_played_tracks.index, hue=most_played_tracks.index, legend=False, palette="viridis")
plt.title("Top 100 Most Played Tracks")
plt.xlabel("Total Minutes Played")
plt.ylabel("Track Name")
plt.show()

print("... 2. Top 15 Artists")
most_played_artists = combined_df.groupby("master_metadata_album_artist_name")["minutes_played"].sum().nlargest(15)
plt.figure(figsize=(12, 8))
sns.barplot(x=most_played_artists.values, y=most_played_artists.index, hue=most_played_artists.index, legend=False, palette="plasma")
plt.title("Top 15 Most Played Artists")
plt.xlabel("Total Minutes Played")
plt.ylabel("Artist Name")
plt.show()

print("... 3. Yearly Trend")
yearly_usage = combined_df.groupby("year")["minutes_played"].sum().reset_index()
plt.figure(figsize=(10, 5))
sns.lineplot(data=yearly_usage, x="year", y="minutes_played", marker="o", color="blue")
plt.title("Total Listening Time by Year")
plt.ylabel("Minutes Played")
plt.xticks(yearly_usage["year"].unique())
plt.grid(True)
plt.show()

print("... 4. Top Artists Per Year")
artist_yearly = combined_df.groupby(["year", "master_metadata_album_artist_name"])["minutes_played"].sum().reset_index()
top_artists_per_year = artist_yearly.sort_values(["year", "minutes_played"], ascending=[True, False]).groupby("year").head(10)
plt.figure(figsize=(14, 7))
sns.barplot(data=top_artists_per_year, x="year", y="minutes_played", hue="master_metadata_album_artist_name", palette="tab20")
plt.title("Top 10 Artists by Year")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

print("... 5. Artist Growth")
target_artist = "Drake"
if target_artist not in combined_df["master_metadata_album_artist_name"].values:
    target_artist = most_played_artists.index[0]

artist_growth = combined_df[combined_df["master_metadata_album_artist_name"] == target_artist].groupby("year")["minutes_played"].sum().reset_index()
plt.figure(figsize=(10, 5))
sns.lineplot(data=artist_growth, x="year", y="minutes_played", marker="o", color="purple")
plt.title(f"Growth over the years: {target_artist}")
plt.ylabel("Minutes Played")
plt.xticks(artist_growth["year"].unique())
plt.grid(True)
plt.show()

print("... 6. Artist Discoveries")
first_listens = combined_df.dropna(subset=["master_metadata_album_artist_name"]).groupby("master_metadata_album_artist_name")["timestamp"].min().reset_index()
first_listens["year_discovered"] = first_listens["timestamp"].dt.year
discoveries = first_listens["year_discovered"].value_counts().sort_index().reset_index()
discoveries.columns = ["year", "new_artists"]
plt.figure(figsize=(10, 5))
sns.barplot(data=discoveries, x="year", y="new_artists", hue="year", legend=False, palette="mediumseagreen")
plt.title("New Artists Discovered Per Year")
plt.show()

print("... 7. Heatmap")
monthly_artist_usage = combined_df.groupby(["master_metadata_album_artist_name", "month_year"])["minutes_played"].sum().unstack(fill_value=0)
top_20_heatmap = monthly_artist_usage.loc[most_played_artists.index] 
plt.figure(figsize=(14, 8))
sns.heatmap(top_20_heatmap, cmap="YlGnBu", linewidths=0.3, linecolor='gray')
plt.title("Listening Heatmap: Top Artists Over Time")
plt.xlabel("Month")
plt.ylabel("Artist")
plt.tight_layout()
plt.show()

print("... 8. Monthly Activity")
monthly_listens = combined_df.groupby('month_year')['minutes_played'].sum()
monthly_listens.index = monthly_listens.index.astype(str)
plt.figure(figsize=(14, 6))
monthly_listens.plot(kind='bar', color='skyblue')
plt.title("Minutes Played Per Month")
plt.ylabel("Total Minutes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("... 9. Hourly Trend")
hourly_trend = combined_df.groupby("hour")["minutes_played"].sum()
plt.figure(figsize=(10, 5))
hourly_trend.plot(kind="bar", color="lightgreen")
plt.title("Listening Trend by Hour of Day")
plt.xlabel("Hour (24h)")
plt.ylabel("Total Minutes")
plt.show()

print("... 10. Day of Week Trend")
days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekday_trend = combined_df.groupby("day_of_week")["minutes_played"].sum().reindex(days_order)
plt.figure(figsize=(10, 5))
sns.barplot(x=weekday_trend.index, y=weekday_trend.values, hue=weekday_trend.index, legend=False, palette="coolwarm")
plt.title("Listening Trend by Day of Week")
plt.ylabel("Total Minutes")
plt.show()

print("DONE. All graphs have been saved to the 'output/graphs' folder.")