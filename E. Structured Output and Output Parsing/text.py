from langchain_core.messages import HumanMessage, SystemMessage , AIMessage
from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()

sys=    SystemMessage(content="You are a helpful assistant! Your name is Bob."),
human =    HumanMessage(content="What is your name?"),
ai =    AIMessage(content="My name is Bob. How can I assist you today?")

print(sys)
print("="*100)
print(human)
print("="*100)
print(ai)
print("="*100)
print(parser.parse(ai.content)) # type: ignore 