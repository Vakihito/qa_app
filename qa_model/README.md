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
    "context":  "I'm sad because I have too much work",
    "question": "why I'm sad ?"
}
```