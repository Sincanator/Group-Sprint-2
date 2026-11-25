NEEDS CLEANING (NOT DONE YET)

We wanted our performance metric to allow us to appropriately compare our different models without bias towards a particular model. 

Initially we discussed the idea of using a simple metric which was just overall percentage accuracy of the predictions. However after some research, we found out that this is not a good measure if we have imbalanced data. Our model would classify each data point into one of four classes, which means that under a binary framework, our data becomes imbalanced. This is because if we are looking at a specific data point and want to see if it was classifed as 'Happy' or 'Not Happy', then the split becomes 25/75 as the 'Not Happy' category would include the other 3 classes ('Sad', 'Relaxed', and 'Angry'). So this metric would not be suitable.

We also discussed using specificity and sensitivity as a metric, with the aim being to minimise the false positives and false negatives. But we talked about how there is a subjective nature around which one of these is worse if it were to occur.

After further research and discussion we settled on using the F1 score as our metric. We decided that this would be suitable because...