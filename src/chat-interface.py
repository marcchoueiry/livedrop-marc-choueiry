import requests

ngrok_url = input("Enter your ngrok public URL (e.g., https://xxxxxx.ngrok.io): ")

def ask_llm(question):
    try:
        response = requests.post(
            f"{ngrok_url}/query", 
            json={"question": question},
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            answer = data.get("answer", "No answer returned.")
            sources = data.get("sources", "No sources.")
            confidence = data.get("confidence", "Unknown")
            print("\nAnswer:", answer)
            print("Sources:", sources)
            print("Confidence:", confidence, "\n")
        else:
            print("Error: LLM returned status code", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Connection error:", e)

print("Welcome to your LLM chat interface! Type 'exit' to quit.\n")

while True:
    question = input("> ")
    if question.lower() in ["exit", "quit"]:
        print("Exiting chat interface.")
        break
    print("[Retrieving context...]\n[Calling LLM...]")
    ask_llm(question)
