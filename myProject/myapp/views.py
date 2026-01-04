from django.shortcuts import render
from .ai import ask_ai  # import the AI function

def ai_chat(request):
    """
    Handles chat requests from the user.
    """
    last_prompt = ""
    answer = ""

    if request.method == "POST":
        last_prompt = request.POST.get("prompt", "").strip()
        if last_prompt:
            answer = ask_ai(last_prompt)
        else:
            answer = "Please enter a prompt."

    # Input box will always be empty after sending
    context = {
        "last_prompt": last_prompt,  # show user prompt below form
        "answer": answer             # show AI answer
    }

    return render(request, "myapp/chat.html", context)

def about(request):
    return render(request, 'myapp/about.html')