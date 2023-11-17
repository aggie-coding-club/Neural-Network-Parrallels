#import openai

# Set your API key here (if not using an environment variable)
#openai.api_key = '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'
#from openai 
from openai import OpenAI

client = OpenAI(api_key='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') #not secure but whatever



def get_summary(text):
    try:
        response = client.completions.create(#engine="text-davinci-003",
        #response = openai.Completion.create( - depreciated
            model="text-davinci-003",  # Model you're using
            prompt=f"{text}\n\ntl;dr:",  # Gives the model the input, then says tl;dr afterwards for summary
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
