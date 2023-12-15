from dotenv import load_dotenv
import os
from openai import OpenAI
import pprint
from halo import Halo

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(messages):
    spinner = Halo(text='Loading...', spinner='dots')
    spinner.start()

    model_name = os.getenv("MODEL_NAME")

    response = client.chat.completions.create(model=model_name,
        messages=messages,
        temperature=0.5,
        max_tokens=250
    )

    spinner.stop()

    pp = pprint.PrettyPrinter(indent=4)
    print("Request:")
    pp.pprint(messages)

    response_message = response.choices[0].message.content
    print(response_message)
    return response_message

def main():
    messages=[
        {"role": "system", "content": "You are a kind and wise therapist, looking to give advice and help people with personal problems."}
        ]

    while True:
        input_text = input("You: ")
        if input_text.lower() == "quit":
            break

        messages.append({"role": "user", "content": input_text})

        response = generate_response(messages)
        messages.append({"role": "assistant", "content": response})



if __name__ == '__main__':
    main()