# MovieLens Data Schema (Phase 0 Draft)

- ratings.csv (to be used later)
  - userId: int
  - movieId: int
  - rating: float (0.5–5.0)
  - timestamp: int (epoch seconds)

- movies.csv (to be used later)
  - movieId: int
  - title: string
  - genres: string (pipe-separated, e.g., "Adventure|Animation|Comedy")
