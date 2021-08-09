import titanic_ML

def prediction_model(pclass, sex, age, sibsp, parch, fare, embarked, title):
  import pickle
  import os.path
  x = [[pclass, sex, age, sibsp, parch, fare, embarked, title]]
  randomforest = pickle.load(open(os.path.join('titanic_ML','titanic_model.sav'),'rb'))
  prediction = randomforest.predict(x)
  return 'Survived' if prediction == 1 else 'Not Survived'