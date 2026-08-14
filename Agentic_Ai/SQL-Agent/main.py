from agent import agent


question = input("Ask a database question: ")

answer = agent(question)

print("\nFINAL ANSWER:")
print(answer)