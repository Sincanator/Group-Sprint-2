We wanted our performance metric to allow us to appropriately compare our different models without bias towards a particular model. Initially we discussed the idea of using a simple metric which was just overall percentage accuracy of the predictions. However after some research, we found out that this is not a good measure if we have imbalanced data 



Copied from notes: Overall dog emotion accuracy % Doesn't work for imbalanced data, our data is imbalanced under a binary framework because the split becomes 25/75 so this metric isn't great for our project. Our data set classifies 4 different emotions with 1,000 datapoints each (so 4,000 total). Suppose it's Happy vs Not Happy in our model, then it becomes 1,000 vs 3,000 and so our data is imbalanced under this binary framework.