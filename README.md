# Movie Recommendation System

A recommendation system built on the MovieLens 20M dataset comparing collaborative filtering and content-based approaches for cold-start movie scenarios.

## Project Structure
`````
movielens-recommender/
├── notebooks/
│   ├── 01_preprocessing.ipynb
│   ├── 02_baseline_cf.ipynb
│   └── 03_content_based.ipynb
├── data/
│   ├── df_train.csv
│   └── df_test.csv
├── results/
│   ├── baseline_metrics.json
│   └── content_based_diagnostics.png
├── requirements.txt
└── README.md
`````

## Dataset

**Source:** [MovieLens 20M](https://grouplens.org/datasets/movielens/20m/)
- 20M ratings from 138K users on 27K movies
- Rating scale: 0.5-5.0 stars
- Time period: 1995-2015

## Methodology

### 1. Data Preprocessing & Feature Engineering

The MovieLens 20M dataset was preprocessed to create a realistic evaluation framework for cold-start recommendations. Feature engineering focused on three categories: temporal features (rating_year, rating_month, rating_dow, movie_age) to capture time-based patterns, user behavioral features (user_avg_rating, user_rating_std, user_n_ratings, user_activity_span) to model individual rating tendencies, and movie popularity features (movie_avg_rating, movie_rating_std, movie_rating_count) to encode aggregate reception.

A user-stratified time-based train-test split was implemented to ensure realistic evaluation conditions. This approach guarantees all users appear in both training and test sets (avoiding cold-start user scenarios) while using chronologically earlier ratings for training and later ratings for testing. This strategy identified 100 cold-start movies—movies that appear in the test set but have no ratings in the training set—providing a focused evaluation of how each model handles new items without historical interaction data.


### 2. Baseline: Collaborative Filtering with SVD

The baseline model employs matrix factorization through Singular Value Decomposition (SVD) using the Surprise library. SVD decomposes the sparse user-movie rating matrix into lower-dimensional latent factor representations, learning 100-dimensional vectors for both users and movies. The model was trained for 20 epochs with a learning rate of 0.005 and L2 regularization of 0.02 to prevent overfitting.

This approach makes predictions by computing the dot product of user and movie latent vectors, effectively capturing implicit patterns such as "users who rated movies in cluster A similarly also rate movies in cluster B similarly." For cold-start movies, SVD leverages learned user biases (the tendency of a user to rate above or below the global average) and global baseline predictors, enabling reasonable predictions even without direct movie interaction history. The model achieved an RMSE of 0.8359 on the cold-start test set, establishing a strong baseline for comparison.

### 3. Content-Based Filtering with TF-IDF

Content-based filtering was implemented to explicitly leverage movie genre information for cold-start predictions. The approach begins with TF-IDF (Term Frequency-Inverse Document Frequency) vectorization of genre labels, creating 20-dimensional vectors where rare genres receive higher weights.

User genre preference profiles are constructed by taking a weighted average of TF-IDF vectors from all movies the user has rated in the training set. Higher-rated movies contribute more weight to the profile.Cosine similarity between user profiles and movie vectors produces similarity scores between 0-1 (non-negative vectors). The formula `predicted_rating = user_avg_rating + (similarity - 0.5) × 1.0` converts similarity to ratings, with the scaling factor chosen through iterative refinement to avoid overprediction. The final implementation achieved an RMSE of 0.8973 on cold-start movies, performing 7.35% worse than the collaborative filtering baseline.


## Results and Analysis

| Model | RMSE | MAE | Performance |
|-------|------|-----|-------------|
| **SVD Baseline** | 0.8359 | 0.6353 | -- |
| **Content-Based (TF-IDF)** | 0.8973 | 0.6741 | -7.35% |


The SVD baseline achieved RMSE of 0.8359 on 100 cold-start movies (257 test ratings), while content-based TF-IDF achieved 0.8973 RMSE, performing 7.35% worse. Despite lacking explicit genre information, SVD outperformed genre-based filtering because it learns latent quality signals through collaborative patterns — when many users rate a movie highly, its learned representation encodes implicit quality characteristics. The model also leverages user biases (some users consistently rate 0.5 stars above average) and global baseline predictors, enabling reasonable predictions even for unseen movies.

Content-based underperformance stems from three limitations: 
(1) Limited Feature Space — genre labels alone (20 categories) cannot capture the multidimensional factors driving user preferences such as director, cast, cinematography...etc.These nuanced elements heavily influence ratings but are invisible to a genre-only model.

(2) Quality Blindness — the model cannot distinguish quality within genre categories. If a user prefers Sci-fi|Action movies, the model will not differentiate between a high-quality and low-quality Sci-fi|Action movie. Both will have the same similarity score and will be rated highly, despite potentially vast differences in actual user satisfaction.

(3) Regression to Mean — the weighted averaging approach and cosine similarity naturally produce predictions clustering in the 3.0-4.5 range. The model struggles to confidently predict very low ratings (<2.0) or perfect scores (5.0), compressing its prediction range and reducing ability to match the full spectrum of actual ratings.

### Diagnostic Insights

<img width="871" height="291" alt="image" src="https://github.com/user-attachments/assets/d7ca6fbd-ced3-4554-943d-983ed5c56912" />


Diagnostic analysis revealed well-calibrated predictions (mean 3.43 vs actual 3.38) with no systematic bias (errors centered at zero), but high variance as the key weakness. Scatter plots show predictions varying by 2-3 stars for the same actual rating, stemming from inability to distinguish quality within genres. Error distribution ranges from -2 to +3 stars with slight right skew, indicating occasional severe overpredictions when users like a genre but encounter poorly-made examples. The model rarely predicts below 2.0 or at 5.0, instead regressing toward 3.0-4.5 range due to weighted averaging smoothing.


## Next Steps

This recommendation system provides a foundation for cold-start analysis and reveals the limitations of genre-only features. Several extensions could enhance performance:

(1) Enriched Content Features - incorporate richer metadata and user review sentiments This would address quality blindness by enabling distinction between high and low-quality films within genres.

(2) Neural Collaborative Filtering - implement deep learning that combines collaborative signals with side features through user/movie embedding layers, feature concatenation, and deep neural networks. 

(3) Hybrid Ensemble Approach - combine collaborative filtering (for warm items) and enhanced content-based (for cold-start) to optimize predictions. 


## Technologies

**Python 3.8+** | pandas | numpy | scikit-learn | scikit-surprise | matplotlib | seaborn

## 📦 Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Download MovieLens 20M dataset
# https://grouplens.org/datasets/movielens/20m/
# Extract to data/ folder
```

## Usage

Run notebooks in order:
```bash
jupyter notebook notebooks/01_preprocessing.ipynb
jupyter notebook notebooks/02_baseline_cf.ipynb
jupyter notebook notebooks/03_content_based.ipynb
```


