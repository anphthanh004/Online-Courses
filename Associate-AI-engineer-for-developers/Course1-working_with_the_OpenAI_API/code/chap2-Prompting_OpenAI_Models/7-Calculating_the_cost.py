# Calculating the cost
# Before deploying AI features at scale, it's essential to estimate costs. The cost is dependent on the number of input and output tokens used and the model chosen.

# Your task is to calculate the cost of summarizing customer chat transcripts.

# The OpenAI client, along with text, prompt, and max_completion_tokens, are preloaded for you.

# Instructions
# 100 XP
# Extract the input token usage from the response.
# Complete the cost calculation to add the output token cost.

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens=max_completion_tokens
)

input_token_price = 0.15 / 1000000
output_token_price = 0.6 / 1000000

# Extract token usage
input_tokens = response.usage.prompt_tokens
output_tokens = max_completion_tokens
# Calculate cost
cost = (input_tokens * input_token_price + output_tokens * output_token_price)
print(f"Estimated cost: ${cost}")
