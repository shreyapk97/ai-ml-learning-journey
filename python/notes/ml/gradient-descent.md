Gradient Descent Intuition

Learning Rate
The learning rate controls how large each weight update is.

Too large → may overshoot the minimum MSE
Too small → training becomes very slow
Appropriate value → converges efficiently
Iteration
One iteration consists of:

Make predictions
Calculate error/MSE
Update weights and bias
1 iteration = 1 weight update + 1 bias update

Goal of Gradient Descent
Repeatedly update weights and bias to reduce MSE.

Lower MSE → Better predictions

Important
The number of iterations does not tell us whether the minimum MSE has been reached.

Example:

100 iterations = 100 updates of weights and bias.
