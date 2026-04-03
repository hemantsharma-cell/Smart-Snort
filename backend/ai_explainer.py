import ollama

def get_ai_explanation(rule_name: str, raw_text: str):
    prompt = f"""
    You are a cybersecurity expert.
    Explain this Snort rule in simple terms for a beginner:
    Rule Name: {rule_name}
    Raw Text: {raw_text}
    """
    try:
        response = ollama.chat(model='llama3.2', messages=[
            {
                'role': 'user',
                'content': prompt,
            },
        ])
        return response['message']['content']
    except Exception as e:
        print(f"Could not connect to AI: {e}")
        return "AI explanation not available."

if __name__ == "__main__":
    test_explanation = get_ai_explanation(
        rule_name="GPL WEB_SERVER directory traversal",
        raw_text="09/30-20:01:15.823656 [**] [1:2101411:7] GPL WEB_SERVER directory traversal [**] {TCP} 203.0.113.55:48123 -> 192.168.1.10:80"
    )
    print(f"🤖 AI Says:\n{test_explanation}")