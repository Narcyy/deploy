from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

model = ChatOpenAI(model="gpt-4o-mini")


# messages = [
#     SystemMessage ("Translate the human message from english intlo italian"),
#     HumanMessage("Hello")
# ]
# response = model.stream(messages)
# for token in response:

#     print(token.content, end="-")


from langchain_core.prompts import ChatPromptTemplate

# system_template = "Translate the following from English into {language}"

# prompt_template = ChatPromptTemplate.from_messages(
#     [("system", system_template),
#      ("user", "{text}")]
# )

# prompt = prompt_template.invoke({"language":"Italian",
#                                  "text":"Hello"})

# response =model.invoke(prompt)
# print(response)

messages_list= []

system_message = SystemMessage("You are an helpful AI Assistant!")
messages_list.append(system_message)
while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    messages_list.append(query)

    messages_list.append(HumanMessage(query))

    prompt = model.invoke(messages_list)

    response = prompt.content
    messages_list.append(response)

    print(f"AI: {response}")



