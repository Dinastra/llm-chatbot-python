from openai import OpenAI

# Cria o cliente usando a variável de ambiente OPENAI_API_KEY
client = OpenAI()

def main():
    print("🤖 Chatbot LLM em Python")
    print("Digite 'sair' para encerrar.\n")

    system_message = {
        "role": "system",
        "content": (
            "Você é um assistente amigável que responde SEMPRE em português. "
            "Ajude a usuária Evelyn, estudante de ADS, com dúvidas de programação, "
            "front-end, UX/UI, Python e carreira na área de tecnologia. "
            "Responda de forma clara, direta e acolhedora."
        )
    }

    history = [system_message]

    while True:
        user_input = input("Você: ").strip()

        if user_input.lower() in ("sair", "exit", "quit"):
            print("Bot: Foi ótimo falar com você! Até mais 👋")
            break

        if not user_input:
            continue

        history.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=history,
                temperature=0.7,
            )

            answer = response.choices[0].message.content.strip()
            print(f"Bot: {answer}\n")

            history.append({"role": "assistant", "content": answer})

        except Exception as e:
            print("❌ Ocorreu um erro ao falar com o modelo:")
            print(e)
            break


if __name__ == "__main__":
    main()
