# Find and replace
# Find-and-replace tools have been around for decades, but they are often limited to identifying and replacing exact words or phrases. You've been provided with a block of text discussing cars, and you'll use a chat completion model to update the text to discuss planes instead, updating the text appropriately.

# Warning: if you send many requests or use lots of tokens in a short period, you may hit your rate limit and see an openai.error.RateLimitError. If you see this error, please wait a minute for your quota to reset and you should be able to begin sending more requests.


# Instructions
# 100 XP
# Create a request to the Chat Completions endpoint; use a maximum of 100 tokens.
# Extract and print the text response from the API.

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

prompt="""Replace car with plane and adjust phrase:
A car is a vehicle that is typically powered by an internal combustion engine or an electric motor. It has four wheels, and is designed to carry passengers and/or cargo on roads or highways. Cars have become a ubiquitous part of modern society, and are used for a wide variety of purposes, such as commuting, travel, and transportation of goods. Cars are often associated with freedom, independence, and mobility."""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}],
  max_completion_tokens=100,
)

# Extract and print the response text
print(response.choices[0].message.content)
# print(response)
# # Extract and print the response text
# print(response.choices[0].____.____)


# client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# prompt="""Replace car with plane and adjust phrase:
# A car is a vehicle that is typically powered by an internal combustion engine or an electric motor. It has four wheels, and is designed to carry passengers and/or cargo on roads or highways. Cars have become a ubiquitous part of modern society, and are used for a wide variety of purposes, such as commuting, travel, and transportation of goods. Cars are often associated with freedom, independence, and mobility."""

# # Create a request to the Chat Completions endpoint
# response = client.chat.completions.create(
#   model="gpt-4o-mini",
#   messages=[{"role": "user", "content": prompt}],
#   max_completion_tokens=100,
# )

# # Extract and print the response text
# print(response.choices[0].message.content)
# A plane is a vehicle that is typically powered by jet engines or propellers. It has wings and is designed to carry passengers and/or cargo through the sky. Planes have become a ubiquitous part of modern society, and are used for a wide variety of purposes, such as commuting, travel, and transportation of goods over long distances. Planes are often associated with freedom, independence, and mobility.
# client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# prompt="""Replace car with plane and adjust phrase:
# A car is a vehicle that is typically powered by an internal combustion engine or an electric motor. It has four wheels, and is designed to carry passengers and/or cargo on roads or highways. Cars have become a ubiquitous part of modern society, and are used for a wide variety of purposes, such as commuting, travel, and transportation of goods. Cars are often associated with freedom, independence, and mobility."""

# # Create a request to the Chat Completions endpoint
# response = client.chat.completions.create(
#   model="gpt-4o-mini",
#   messages=[{"role": "user", "content": prompt}],
#   max_completion_tokens=100,
# )

# # Extract and print the response text
# # print(response.choices[0].message.content)
# print(response)
# ChatCompletion(id='chatcmpl-D7HJfNnUibygqSHUu5R6eLsq3BqVc', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='A plane is a vehicle that is typically powered by jet engines or propellers. It has wings and is designed to carry passengers and/or cargo through the air. Planes have become a ubiquitous part of modern society and are used for a wide variety of purposes, such as commuting, travel, and transportation of goods. Planes are often associated with freedom, independence, and mobility.', refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=None))], created=1770627231, model='gpt-4o-mini-2024-07-18', object='chat.completion', service_tier='default', system_fingerprint='fp_f4ae844694', usage=CompletionUsage(completion_tokens=76, prompt_tokens=96, total_tokens=172, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0)))
# In [1]:
