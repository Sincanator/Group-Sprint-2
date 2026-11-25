How do neural networks works for classifying emotions?

Found a good paper about it here --> https://arxiv.org/pdf/1105.6014

In introduction it suggests 2 methods for identifying facial expressions: a static approach and a dynamic approach. The static approach classifies each video frame individually into a facial expression category using Bayesian classifiers, focusing on facial features within each frame. The dynamic approach sses Hidden Markov Models (HMMs) to analyse how facial expressions change over time and automatically segment videos into different expression sequences. They use what's called a Facial Expression Recognition system which consists of three key stages: detecting the face, extracting facial features, and classifying the emotion. Paper then dives into the mathematics behind it then in section 5 talks about the design of such a neural network for emotion classfication which goes into a lot of detail.

My specific model's performance so far:

My model was 'densenet121' which has 121 layers. Using the initial unchanged model (4 epochs and 1e-2 learning rate), we get an accuracy of 0.87. But when we changed the learning rate to 4e-4 we get an accuracy of 0.90.

Research for finding optimal number of epochs in google collab code:

I will display the number of epochs used below, with their corresponding accuracy attached with it. These different tests are all run using the same updated learning which is 4e-4.

Epochs = 4, Accuracy = 0.86 (2nd Run)

Epochs = 5, Accuracy = 0.87 (3rd Run)

Epochs = 6, Accuracy = 0.87 (4th Run)

Epochs = 7, Accuracy = 0.87 (5th Run)

Epochs = 8, Accuracy = 0.87 (6th Run)

Epochs = 9, Accuracy = 0.87 (7th Run)

Epochs = 20, Accuracy = 0.88 (8th Run)

Epochs = 30, Accuracy = 0.90 (9th Run)