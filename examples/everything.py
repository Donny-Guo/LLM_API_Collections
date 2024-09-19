import csv, json, os, time
import anthropic
from evaluate import evaluate

def read_data(filename: str) -> tuple:
    # Read JSON file
    with open(filename, 'r') as file:
        data = json.load(file)

    # Extract instructions and answers
    instructions = [item['instruction'] for item in data]
    answers = [item['answer'] for item in data]
    return (instructions, answers)

def get_output(prompt: str) -> tuple:
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
                        "text": prompt,
                    }
                ]
            }
        ]
    )

    model_output = message.content[0].to_dict()['text']
    usage = message.usage.to_dict()
    input_tokens = usage['input_tokens']
    output_tokens = usage['output_tokens']

    return (model_output, input_tokens, output_tokens)

def gather_results(output_filename):
    data = list(zip(instructions, answers, model_outputs))

    # Write to CSV
    with open(output_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Prompt', 'Answer', 'Model Output'])  # Write header
        writer.writerows(data)  # Write data
    
if __name__ == "__main__":
    print("Script starts")
    start_time = time.time()

    client = anthropic.Anthropic(api_key = os.environ.get("ANTHROPIC_API_KEY"))
    datafile = "dataset/test.json"
    output_file = "output/claude-result.csv"
    instructions, answers = read_data(datafile)
    model_outputs = []
    total_input_tokens, total_output_tokens = 0, 0

    # get output by calling APIs
    print("Start API calls......")
    i = 0
    for prompt in instructions:
        model_output, input_tokens, output_tokens = get_output(prompt)
        model_outputs.append(model_output)
        total_input_tokens += input_tokens
        total_output_tokens += output_tokens
        i += 1
        if i % 20 == 0:
            print(f"Finished {i}/{len(instructions)}\n")
    
    print("Finished all API calls.")
    print(f"total_input_tokens: {total_input_tokens}\n")
    print(f"total_output_tokens: {total_output_tokens}\n")
    print(f"total tokens used: {total_input_tokens + total_output_tokens}\n")
    # save results to csv
    gather_results(output_file)
    print("Save results to ", output_file)

    # Evaluate results
    evaluate(output_file)

    end_time = time.time()
    print(f"Script ends. Total runtime: {end_time - start_time:.2f} seconds")