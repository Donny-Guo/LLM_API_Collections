import csv, json, time
from openai import OpenAI
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
    message = client.chat.completions.create(
        model= model_name,
        messages=[
            {"role": "system", "content": "You are an expert in crisis management."},
            {
                "role": "user",
                "content":[
                        {
                            "type": "text",
                            "text": prompt,
                        }]
            }
        ]
    )
    model_output = message.choices[0].message.to_dict()['content']
    usage = message.usage.to_dict()
    input_tokens = usage['prompt_tokens']
    output_tokens = usage['completion_tokens']

    return (model_output, input_tokens, output_tokens)

def gather_results(output_filename, filetype='json'):
    if filetype == 'json':
        data = [
            {"Prompt": inst, "Answer": ans, "Model Output": out}
            for inst, ans, out in zip(instructions, answers, model_outputs)
        ]
        # Write to JSON
        with open(output_filename, 'w') as file:
            json.dump(data, file, indent=4)

    elif filetype == 'csv':
        data = list(zip(instructions, answers, model_outputs))
        # Write to CSV
        with open(output_filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Prompt', 'Answer', 'Model Output'])  # Write header
            writer.writerows(data)  # Write data
    
if __name__ == "__main__":
    client = OpenAI()
    print("Script starts")
    start_time = time.time()
    model_name = "gpt-4o-mini"

    datafile = "dataset/llama_test.json"
    output_file = f"output/openai-{model_name}-result-with-system-prompt.json"
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