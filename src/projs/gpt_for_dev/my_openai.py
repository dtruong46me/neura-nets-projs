from openai import OpenAI

api_key = "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"
client = OpenAI(api_key=api_key)
client.api_key = api_key
print(1)
print(client.api_key)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)
print(response.choices[0].message.content)

