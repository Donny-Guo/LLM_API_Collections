import os
import anthropic

client = anthropic.Anthropic(
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    # api_key="my_api_key",
)

message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000,
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Classify the following tweet for crisis management. Decide if it gives important information that could help during a crisis. Reply with only '1' if the tweet provides useful information, or only '0' if it does not. Tweet: RT @THS_College: On our way to Warrior Restoration to help organize donations for #hurricaneharvey! https://t.co/vMheEvAyew."
                }
            ]
        }
    ]
)
print("message usage: ", message.usage.to_dict())
print("Message content: ", message.content)
print("text:", message.content[0].to_dict()['text'])