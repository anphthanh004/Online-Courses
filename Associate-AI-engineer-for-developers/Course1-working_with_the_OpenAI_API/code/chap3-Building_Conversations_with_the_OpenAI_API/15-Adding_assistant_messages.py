# Adding assistant messages
# Chat models are great for creating conversational applications, but they can be further improved by providing part of a conversation for the model to build on.

# Improve this geography tutor application by including this example student prompt and ideal model response in the messages:

# Example Question: Give me a quick summary of Portugal.
# Example Answer: Portugal is a country in Europe that borders Spain. The capital city is Lisboa.
# Instructions
# 100 XP
# Add the example question and answer provided as a user-assistant pair in the messages sent to the model.
# Example Question: Give me a quick summary of Portugal.
# Example Answer: Portugal is a country in Europe that borders Spain. The capital city is Lisboa.


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    # Add a user and assistant message for in-context learning
    messages=[
        {"role": "system", "content": "You are a helpful Geography tutor that generates concise summaries for different countries."},
        {"role": "user", "content": "Example Question: Give me a quick summary of Portugal."},
        {"role": "assistant", "content": "Example Answer: Portugal is a country in Europe that borders Spain. The capital city is Lisboa."},
        {"role": "user", "content": "Give me a quick summary of Greece."}
    ]
)

print(response.choices[0].message.content)


# Greece is a southeastern European country located on the southern end of the Balkan Peninsula. It is known for its rich ancient history, including being the birthplace of democracy and Western philosophy. The capital city is Athens, which is home to iconic landmarks like the Acropolis. Greece features a diverse landscape with numerous islands, such as Crete and Santorini, and a Mediterranean climate. It is renowned for its contributions to art, literature, and cuisine, making it a popular tourist destination.