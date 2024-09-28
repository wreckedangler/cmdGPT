import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="gpt-3.5-turbo",
    )
    return response.choices[0].message.content

def main():
    while True:
        user_input = input("--> ")
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting...")
            break
        response = chat_with_gpt(user_input)
        print("Jarvis: " + response)


if __name__ == "__main__":
    main()