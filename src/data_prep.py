# src/data_prep.py
import os
import pandas as pd

def main():
    os.makedirs("data/processed", exist_ok=True)
    # Tiny synthetic data to validate the flow
    ratings = pd.DataFrame({
        "userId": [1, 1, 2, 2],
        "movieId": [101, 102, 101, 103],
        "rating": [4.0, 3.5, 5.0, 4.0],
        "timestamp": [1609459200, 1609459300, 1609460000, 1609460100],
    })
    movies = pd.DataFrame({
        "movieId": [101, 102, 103],
        "title": ["Sample A", "Sample B", "Sample C"],
        "genres": ["Drama", "Comedy", "Action"],
    })
    ratings.to_csv("data/processed/ratings_sample.csv", index=False)
    movies.to_csv("data/processed/movies_sample.csv", index=False)
    print("Wrote sample datasets to data/processed/")

if __name__ == "__main__":
    main()
