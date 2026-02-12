<!-- Specifying an OpenAI model
OpenAI offers multiple models for different use cases. In this exercise, you'll specify the model and define the role to structure your API requests.

The OpenAI class has already been imported for you from the openai library.

Instructions
100 XP
Specify the gpt-4o-mini model.
Assign the correct role in the messages list. -->


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
  # Specify the model
  model="gpt-4o-mini",
  messages=[
    # Assign the correct role
    {"role": "user", 
     "content": "Announce my new AI Engineer role on LinkedIn."}]
)

print(response.choices[0].message.content)


<!-- Certainly! Here’s a suggestion for your LinkedIn announcement: -->

<!-- ---

🚀 Exciting News! 🚀

I am thrilled to share that I have accepted a new role as an AI Engineer! 🎉 

I am incredibly grateful for this opportunity to contribute to [Company Name] and work with a talented team dedicated to pushing the boundaries of artificial intelligence and machine learning. 

As I embark on this new journey, I look forward to tackling innovative challenges, building cutting-edge solutions, and continuing to grow in this dynamic field. 

Thank you to everyone who has supported me along the way! Here's to new beginnings and endless possibilities. 

#NewRole #AIEngineer #ArtificialIntelligence #MachineLearning #CareerGrowth

---

Feel free to customize it to better reflect your personality and specific details about your new company or position!
In [1]: -->
