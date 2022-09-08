# Idea
Trading bot that makes use of current information about companie for long-time stock prediction.

Maybe only one stock/company.

# Methodology
- Data:
  - Get new souce
    - Instagram/tiktok/news-outlets
    - https://newsapi.org/
  - Get stock information
    - TBD
  - parse every content w.r.t. the stokes company (e.g. porche)
    - Word2Vec/Bert encoding, etc...
    - Video2Vec/Image2Vec/CLIP encodings, etc...
- bot #1:
  - sort every token by date
  - transformer takes the series of tokens as input and tries to predict whether the stock will rise or fall
- bot #2:
  - emotion analysis on content
    - emotion classifier on text, same for video/images, etc...
  - either:
    1. cluster emotions on timeline
    2. transformer makes final decision
  
