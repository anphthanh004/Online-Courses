# Building an OpenAI API request
# Throughout the course, you'll write Python code to interact with the OpenAI API. Entering your own API key is not necessary to create requests and complete the exercises in this course.

# The OpenAI class has already been imported for you from the openai library.

# Instructions
# 100 XP
# Create an OpenAI API client (keep <OPENAI_API_TOKEN> unchanged).
# create a request to the Chat Completions endpoint.

# Create the OpenAI client
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "user", 
     "content": "Write a polite reply accepting an AI Engineer job offer."}]
)

print(response.choices[0].message.content)


# Subject: Acceptance of Job Offer – AI Engineer Position

# Dear [Hiring Manager's Name],

# I hope this message finds you well. 

# I am writing to formally accept the offer for the AI Engineer position at [Company Name]. I am thrilled about the opportunity to contribute to such an innovative team and am eager to bring my skills and experience to the role.

# Thank you for this incredible opportunity. I am looking forward to joining the team on [start date] and contributing to the exciting projects at [Company Name].

# Please let me know if there are any documents or information needed from my side before my start date.

# Best regards,

# [Your Name]  
# [Your Phone Number]  
# [Your Email Address]