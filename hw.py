import requests
import random

h_api= "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"
def a(text):
  url = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"
  headers={"Authorization":f"Bearer {h_api}"}
  payload={"inputs":text}
  response=requests.post(url,headers=headers,json=payload)
  return response.json()
Sam_text=["i am netural today",
          "I am excited!",
          "I am sad",
          "I am confused"]
result=a(random.choice(Sam_text))
print(result)