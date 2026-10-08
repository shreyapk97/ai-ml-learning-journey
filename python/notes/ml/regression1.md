Linear Regression and Multiple Linear Regression

Linear Regression
Linear Regression predicts a continuous value using one feature.

Equation
y = wX + b

Where:

X = Feature (input)
y = Target (output)
w = Weight (coefficient)
b = Bias (intercept)
Example
Hours Studied → Score

y = 10X + 50

For:

X = 5

Prediction:

y = 10(5) + 50 = 100

Scikit-Learn
model.fit(X, y)
Trains the model
Learns the values of w and b
model.predict([[5]])
Uses the trained model
Predicts the output for a new input

### Model Parameters

```python
model.coef_
Weight (w)
model.intercept_
Bias (b)
Multiple Linear Regression
Multiple Linear Regression predicts a continuous value using multiple features.

Equation
y = w1x1 + w2x2 + ... + wn*xn + b

Where:

x1, x2, ..., xn *re features
w1, w2, ..., wn are *oefficients -bis the intercept
Example
Fea*ures:

Age (x1)
Experience (x2*
Target:

Salary (y)
Equation*

= 1000x1 + 5000x2 + 10000
Co*fficients
If:

X.shape * (100, 2)
Then:

Example:

mode*.coef_ = [5, 10]
Meaning:

= weight for feature 1 -**0 = weight for feature 2
Key *ule
Number of Features = Number o* Coefficients

Examples:

*odel.coef_.shape = (1,)
X.shape = (500, 3)
``*

*``python
model.coef_.shape = (3,)
*``

```python
X.shape = (200, 4)
`*`

```python
model.coef_.shape = (*,)
``*

*--

## Shapes

### Training Data

*``python
X.shape = (samples, featu*es)
Examples:

100 samples
3 feature*
y.shape = (100,)
100 target values
###PredictionInput

For a model with 3 features*

Incorrect:

model.pred*ct([5, 10, 2])
*hape:

*``python (3,)


Correct:

```py*hon
model.predict([[5, 10, 2]])
``*

Shape:

```python
(1, 3)
``*

*cikit-Learn expects prediction inp*t in the form:

```python
(samples* features)
Even for a single *rediction.

*# Key Concepts Learned

Features (X)
Target (y)
Sampl*s vs Features
X.shape and y.shap*
TrainingandPrediction
model.fit()
model.p*edict()
Linear Regression
Mult*ple Linear Regression
model*coef_
model.intercept_
Number of Features = Number of Coefficients
Prediction inputs must be 2D ```
