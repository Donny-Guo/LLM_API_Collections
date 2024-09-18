# LLM_API_Collections
A collection of common LLM API Calls





## 1. Chatgpt

1. install openai library: `pip install openai`



## 2. Anthropic - Claude

### 1. Python

1. Reference: https://docs.anthropic.com/en/docs/initial-setup, https://github.com/anthropics/anthropic-sdk-python

2. Anthropic Python API library: `pip install anthropic`

3. Get API key from https://console.anthropic.com/settings/keys and add it to `~/.zshrc` (Mac) by adding a line `export ANTHROPIC_API_KEY="your_api_key"`. Then do `source ~/.zshrc`

4. Run the following:

   ```python
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
                       "text": "Why sky is blue?"
                   }
               ]
           }
       ]
   )
   print(message.content)
   ```

5. check token usage: https://console.anthropic.com/settings/usage





## 3. Perplexity

API references: https://docs.perplexity.ai/api-reference/chat-completions

Supported model: https://docs.perplexity.ai/guides/model-cards

`llama-3.1-8b-instruct`
