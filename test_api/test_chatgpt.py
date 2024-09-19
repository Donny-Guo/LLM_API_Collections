from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an expert in crisis management."},
        {
            "role": "user",
            "content":[
                    {
                        "type": "text",
                        "text": "Classify the following tweet for crisis management. Decide if it gives important information that could help during a crisis. Reply with only '1' if the tweet provides useful information, or only '0' if it does not. No explanation needed. Tweet: Cristofer CLEMENTE MORA now in 2nd at aguille du posettes. He's hunting \u00e2\u0161\u00a1\u00ef\u00b8\u008f #MontBlancMarathon 80k https://t.co/D7NLD18qWz.",
                    }]
        }
    ]
)
print(completion)
print(completion.choices[0].message)
print(completion.choices[0].message.to_dict()['content'])
usage = completion.usage.to_dict()
input_tokens = usage['prompt_tokens']
output_tokens = usage['completion_tokens']
print("input_tokens: ", input_tokens)
print("output tokens: ", output_tokens)