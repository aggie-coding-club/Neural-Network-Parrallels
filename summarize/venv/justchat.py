from openai import OpenAI

client = OpenAI(api_key='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') #not sure but whatever
# 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 - tony
# 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 - key 2

# Set your API key here (if not using an environment variable)
 #not secure but whatever

def get_summary(text):
    if text == "":
        print("Please give an input")
        return

    try:
        response = client.completions.create(#engine="text-davinci-003",
        #response = openai.Completion.create(
            model="text-davinci-003",  # Model you're using
            #model="gpt-4",
            prompt=f"{text}\n\n Summarize the former text that I inputted, but then explain how it relates to Texas A&M Univerity.",
            temperature=0.9,  # Controls randomness - cranking up 
            max_tokens=150,  # Max length of response
            top_p=1,  # Diversity of output
            frequency_penalty=1,  # Keeps it succinct
            presence_penalty=0)
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    user_input = input("Enter the text you want to summarize: ")
    summary = get_summary(user_input)
    if summary:
        print("\nSummary:")
        print(summary)

if __name__ == "__main__":
    main()