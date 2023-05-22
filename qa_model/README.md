# Build model with bentoml

## 1. serve model api locally
 1. Download one model from the folder located in : [models](https://drive.google.com/drive/folders/1R9WZDyQBQqHQYKkmHsN_yzSx0ZZSDFVz?usp=share_link)

 2. After selecting a model from the folder, unzip the model into the folder "QA_model/model"

## 2. serve model api locally

```
bentoml serve service:svc --port=8000
```


## 3. test sample
after serving the model just test in the `localhost:8000`
```
{
    "context":  "The interface of the app is good and very easy to navigate. Only problem is the drivers cancels the ride 8 out of 10 times I've used Uber. It is really frustrating when you are in a hurry. I think some actions should be put forward for the drivers as well to not cancel the request once accepted. In few instances, despite the driver canceling the ride, I had to pay the penalty fee. What I wrote is an honest opinion, after using Uber to book a ride for several months now.",
    "question": "what is the problem with the drivers ?"
}
```