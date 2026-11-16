- Overall dog emotion accuracy %
Doesn't work for imbalanced data, our data is imbalanced under a binary framework because the split becomes 25/75 so this metric isn't great for our project. Our data set classifies 4 different emotions with 1,000 datapoints each (so 4,000 total). Suppose it's Happy vs Not Happy in our model, then it becomes 1,000 vs 3,000 and so our data is imbalanced under this binary framework.
- % accuracy for each individual emtotion (% for happy accuracy ect)
Might introduce the problem of imbalanced data again? However if we're looking at each individual emotions' accuracy, then this could still be a decent performance metric (not entirely sure though).
- 'Area under curve' idea from Jonty (measuring specificty and sensitivity)
Our aim would be to minimise the false positives/negatives, also discussed the subjective nature of which one would be "worse" if it were to occur (ie, would we rather prevent a false positive or a false negative if we could only prevent one").
- Anna mentioned F1 Score and Precission
Precission uses true positive ect stuff, F1 then uses weights (or Fbeta, F1 just uses weight of 1) and also includes the Precission value.