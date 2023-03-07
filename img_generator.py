import os
import openai
from env_variable import OPENAI_API_KEY
from word_lists import *

# Load your API key from an environment variable or secret management service
openai.api_key = OPENAI_API_KEY

response = openai.Image.create(
  prompt="a white siamese cat",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)