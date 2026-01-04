# myapp/ai.py
import subprocess

def ask_ai(prompt: str) -> str:
    """
    Sends a prompt to the Mistral model via Ollama CLI and returns the response.
    """
    prompt_lower = prompt.strip().lower()

    # Special case: AI name
    if "your name" in prompt_lower or "who are you" in prompt_lower:
        return "Hi! I am Bhuwan's AI assistant."

    try:
        result = subprocess.run(
            ["ollama", "run", "mistral", prompt],
            capture_output=True,
            text=True
        )
        # Return the model output
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"Error from Ollama: {result.stderr.strip()}"
    except FileNotFoundError:
        return "Error: Ollama CLI not found. Make sure it is installed and in PATH."
    except Exception as e:
        return f"Unexpected error: {str(e)}"
