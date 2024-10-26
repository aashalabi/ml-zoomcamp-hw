# Week 4

### Question 1
```
 Install Pipenv
 What's the version of pipenv you installed?
 Use --version to find out
````


```python
!pipenv --version
```

    pipenv, version 2024.2.0
    

# Question 2
```
Use Pipenv to install Scikit-Learn version 1.5.2
What's the first hash for scikit-learn you get in Pipfile.lock?
```

Answer: sha256:03b6158efa3faaf1feea3faa884c840ebd61b6484167c711548fce208ea09445

# Question 3
```
Let's use these models!

PREFIX=https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/master/cohorts/2024/05-deployment/homework
wget $PREFIX/model1.bin
wget $PREFIX/dv.bin

Write a script for loading these models with pickle
Score this client:
{"job": "management", "duration": 400, "poutcome": "success"}

What's the probability that this client will get a subscription?
```


```python
PREFIX='https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/master/cohorts/2024/05-deployment/homework'
!curl -O {PREFIX}/model1.bin
!curl -O wget {PREFIX}/dv.bin
```

      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    
      0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
    100   850  100   850    0     0   8819      0 --:--:-- --:--:-- --:--:--  9239
    


```python
import pickle

with open('model1.bin', 'rb') as m:
    model = pickle.load(m)

with open('dv.bin', 'rb') as d:
    dv = pickle.load(d)
```

    c:\Users\ahmed\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\base.py:318: UserWarning: Trying to unpickle estimator LogisticRegression from version 1.5.2 when using version 1.2.2. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:
    https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations
      warnings.warn(
    c:\Users\ahmed\AppData\Local\Programs\Python\Python311\Lib\site-packages\sklearn\base.py:318: UserWarning: Trying to unpickle estimator DictVectorizer from version 1.5.2 when using version 1.2.2. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:
    https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations
      warnings.warn(
    


```python
client = {"job": "management", "duration": 400, "poutcome": "success"}
X = dv.transform([client])
y_pred = model.predict_proba(X)[:, 1]
print('Q3 Answer :',  y_pred)
```

    Q3 Answer : [0.90850089]
    


```python

```

# Question 4
```
Now let's serve this model as a web service

Install Flask and gunicorn (or waitress, if you're on Windows)
Write Flask code for serving the model
Now score this client using requests:
url = "YOUR_URL"
client = {"job": "student", "duration": 280, "poutcome": "failure"}
requests.post(url, json=client).json()

What's the probability that this client will get a subscription?
```


```python
import requests

url = 'http://localhost:9696/predict'

client = {"job": "student", "duration": 280, "poutcome": "failure"}
response = requests.post(url, json=client).json()


print('Q4, client probability', response)
```

    Q4, client probability {'churn': False, 'churn_probability': 0.33480703475511053}
    

## Question 5
```
Download the base image svizor/zoomcamp-model:3.11.5-slim. You can easily make it by using docker pull command.

So what's the size of this base image?

45 MB
130 MB
245 MB
330 MB
```


```python
!docker images | findstr svizor/zoomcamp-model
```

    svizor/zoomcamp-model                           3.11.5-slim        975e7bdca086   7 days ago      130MB
    

Answer: 130MB

## Question 6
```
Now create your own Dockerfile based on the image we prepared.

It should start like that:

FROM svizor/zoomcamp-model:3.11.5-slim
# add your stuff here
Now complete it:

Install all the dependencies form the Pipenv file
Copy your Flask script
Run it with Gunicorn
After that, you can build your docker image.

run your docker container!

After running it, score this client once again:

url = "YOUR_URL"
client = {"job": "management", "duration": 400, "poutcome": "success"}
requests.post(url, json=client).json()
What's the probability that this client will get a subscription now?
```

```
docker build -t zoom-camp-wk5 .
docker run -d --name zoom-camp-wk5_1 -p 9696:9696 zoom-camp-wk5
docker ps
docker stop zoom-camp-wk5_1

```


```python
url = 'http://localhost:9696/predict'

client = {"job": "management", "duration": 400, "poutcome": "success"}
response = requests.post(url, json=client).json()


print('Q6, client probability', response)
```

    Q6, client probability {'churn': True, 'churn_probability': 0.756743795240796}
    


```python

```
