from langchain_ollama import ChatOllama
from chains.joke_chain import generate_joke
from chains.Summary_generator_chain import generate_summary_with_streaming
from chains.Motivational_quote_generator_prompt import generate_motivational_quote_with_batch

llm = ChatOllama(
    model="mistral",
    temperature=0.8, 
)

def joke():
    topic = input("Enter the topic for the joke: ").strip()
    joke = generate_joke(topic, llm)
    print(f"Joke about {topic}:\n{joke}")
    
def motivational_quotes():
    topics = input("Enter the topics for the motivational quotes, separated by commas: ").strip().split(",")
    quotes = generate_motivational_quote_with_batch(topics, llm)
    for topic, quote in zip(topics, quotes):
        print(f"Motivational quote about {topic}:\n{quote}\n")

def generate_summary():
    text = input("Enter the text you want to summarize: ").strip()
    generate_summary_with_streaming(text, llm)
    
    
def main():
    print("User you want to generate a joke, motivational quotes or a summary?")
    user = input("Enter 'joke', 'quotes', or 'summary': ").strip().lower()
    if user == "joke":
        joke()
    elif user == "quotes":
        motivational_quotes()
    elif user == "summary":
        generate_summary()
    else:
        print("Invalid input. Please enter 'joke', 'quotes', or 'summary'.")
        
        
if __name__ == "__main__":
    main()