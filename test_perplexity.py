import requests, os
from openai import OpenAI

url = "https://api.perplexity.ai/chat/completions"
api_key = os.environ.get("PERPLEXITY_API_KEY")
prompt = "Classify the following tweet for crisis management. Decide if it gives important information that could help during a crisis. Reply with only '1' if the tweet provides useful information, or only '0' if it does not. Tweet: Cristofer CLEMENTE MORA now in 2nd at aguille du posettes. He's hunting \u00e2\u0161\u00a1\u00ef\u00b8\u008f #MontBlancMarathon 80k https://t.co/D7NLD18qWz."
prompt = "Classify the following tweet for crisis management. Decide if it gives important information that could help during a crisis. Reply with only '1' if the tweet provides useful information, or only '0' if it does not. Tweet: RT @THS_College: On our way to Warrior Restoration to help organize donations for #hurricaneharvey! https://t.co/vMheEvAyew."

payload = {
    "model": "llama-3.1-8b-instruct",
    "messages": [
        {
            "role": "user",
            "content": [
                    {
                        "type": "text",
                        "text": prompt,
                    }]
        }
    ]
}
headers = {
    "Authorization": "Bearer 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",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)
if response.status_code == 200:
    data = response.json()
    # print(type(data))
    # print(data)
    print("output: ", data['choices'][0]['message']['content'])
else:
    print(f"Request failed with status code: {response.status_code}")


# messages = [
#     {
#         "role": "system",
#         "content": (
#             "You are an artificial intelligence assistant and you need to "
#             "engage in a helpful, detailed, polite conversation with a user."
#         ),
#     },
#     {
#         "role": "user",
#         "content": (
#             "How many stars are in the universe?"
#         ),
#     },
# ]

# client = OpenAI(api_key=api_key, base_url="https://api.perplexity.ai")

# # chat completion without streaming
# response = client.chat.completions.create(
#     model="llama-3.1-8b-instruct",
#     messages=messages,
# )
# print("response: ", response)
# print("response text:", response.text)


# payload = {
#     "model": "llama-3.1-8b-instruct",
#     "messages": [
#         {
#             "role": "system",
#             "content": "Be precise and concise."
#         },
#         {
#             "role": "user",
#             "content": "How many stars are there in our galaxy?"
#         }
#     ],
#     "max_tokens": "Optional",
#     "temperature": 0.2,
#     "top_p": 0.9,
#     "return_citations": True,
#     "search_domain_filter": ["perplexity.ai"],
#     "return_images": False,
#     "return_related_questions": False,
#     "search_recency_filter": "month",
#     "top_k": 0,
#     "stream": False,
#     "presence_penalty": 0,
#     "frequency_penalty": 1
# }
# headers = {
#     "Authorization": f"Bearer {api_key}",
#     "Content-Type": "application/json"
# }

# response = requests.request("POST", url, json=payload, headers=headers)

# print("response: ", response)
# print("response text:", response.text)
