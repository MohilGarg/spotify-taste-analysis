# Spotify Taste Analysis

A self-contained tool for analysing your Spotify listening habits through data visualisation, with a planned extension for recommending songs from new playlists based on your existing taste.

Built using Python, pandas, matplotlib, and seaborn.

---

## How It Works

### Step 1 — Export your playlist
Use [Exportify](https://exportify.net) or a similar tool to export your Spotify playlist as a CSV file. Exportify includes audio features (Energy, Valence, Danceability, etc.) alongside track metadata, which is what this project relies on.

### Step 2 — Clean your data
Run the cleaning script to remove any duplicate tracks introduced during export:

```bash
python clean.py your_playlist.csv
```

This outputs a cleaned CSV (`your_playlist_cleaned.csv`) in the same directory.

### Step 3 — Run the analysis
Open `taste_analysis.ipynb` in VS Code or Jupyter and run all cells. The notebook walks through your listening habits section by section, from artist breakdowns to audio feature analysis.

---

## Requirements

Install dependencies with:

```bash
pip install pandas matplotlib seaborn
```

Python 3.8 or above recommended.

---

## Planned Features

- **Song recommender** — provide a CSV of any Spotify playlist and the tool will rank its tracks by how well they match your listening taste, based on audio feature similarity.
