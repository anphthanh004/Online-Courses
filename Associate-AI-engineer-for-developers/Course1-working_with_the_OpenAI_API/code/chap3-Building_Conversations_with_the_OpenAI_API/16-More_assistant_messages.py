# More assistant messages!
# Expand on your previous messages to provide additional examples, stored as example1, response1, example2, response2, example3, and response3.

# Let's see if we can get this model outputting information in the desired format!

# Instructions
# 100 XP
# Expand your previous messages to include additional examples of other countries, which are stored as example1, response1, example2, response2, example3, and response3.


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
   model="gpt-4o-mini",
   # Add in the extra examples and responses
   messages=[
       {"role": "system", "content": "You are a helpful Geography tutor that generates concise summaries for different countries."},
       {"role": "user", "content": "Give me a quick summary of Portugal."},
       {"role": "assistant", "content": "Portugal is a country in Europe that borders Spain. The capital city is Lisboa."},
       {"role": "user", "content": "Give me a quick summary of Việt Nam."},
       {"role": "assistant", "content": "Việt Nam is a Southeast Asian country stretching along the eastern edge of the Indochinese Peninsula, with a long coastline on the South China Sea. It shares borders with China, Laos, and Cambodia, and has two major cities: Hà Nội (the capital, in the north) and Hồ Chí Minh City (the largest, in the south)."},
       {"role": "user", "content": "Give me a quick summary of Nhật Bản."},
       {"role": "assistant", "content": "Nhật Bản (Japan) là một quốc đảo ở Đông Á, nằm trên Thái Bình Dương, gồm bốn đảo chính: Honshu, Hokkaido, Kyushu và Shikoku. Thủ đô là Tokyo – một trong những đô thị lớn và hiện đại nhất thế giới."},
       {"role": "user", "content": "Give me a quick summary of Hàn Quốc."},
       {"role": "assistant", "content": "Hàn Quốc (South Korea) là một quốc gia ở Đông Á, nằm ở nửa phía nam bán đảo Triều Tiên, với thủ đô là Seoul – một trong những trung tâm công nghệ và văn hóa sôi động nhất châu Á."},
       {"role": "user", "content": "Give me a quick summary of Greece."}
   ]
)

print(response.choices[0].message.content)


# Greece is a southeastern European country known for its rich history and contributions to art, philosophy, and politics. It consists of a mainland and numerous islands in the Aegean and Ionian Seas. The capital city is Athens, famous for ancient landmarks like the Acropolis. Greece is recognized as the cradle of Western civilization and has a diverse landscape of mountains and coastal areas.