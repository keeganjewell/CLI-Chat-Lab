#!/usr/bin/env python3
import sys
from pathlib import Path
from llama_cpp import Llama

MODEL_PATH = Path("models/qwen2.5-0.5b/qwen2.5b-q4_k_m.gguf")

# Model parameters
N_CTX = 4096
N_THREADS = 4
N_BATCH = 256

# System prompt (sets the bot's style)
SYSTEM_PROMPT = (
    "You are a helpful teaching assistant. Keep answers concise, "
    "but include clarifying steps when appropriate."
)

print(f"Loading model: {MODEL_PATH} …", file=sys.stderr)
llm = Llama(
    model_path=str(MODEL_PATH),
    n_ctx=N_CTX,
    n_threads=N_THREADS,
    n_batch=N_BATCH,
    verbose=False,
)

history = [{"role": "system", "content": SYSTEM_PROMPT}]

print("\nCLI chatbot ready. Type 'exit' or 'quit' to leave.\n")

while True:
    try:
        user = input("you › ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nbye! ")
        break
#!/usr/bin/env python3
import sys
from pathlib import Path
from llama_cpp import Llama

MODEL_PATH = Path("models/qwen2.5-0.5b/qwen2.5b-q4_k_m.gguf")

# Model parameters
N_CTX = 4096
N_THREADS = 4
N_BATCH = 256

# System prompt (sets the bot's style)
SYSTEM_PROMPT = (
    "You are a helpful teaching assistant. Keep answers concise, "
    "but include clarifying steps when appropriate."
)

print(f"Loading model: {MODEL_PATH} …", file=sys.stderr)
llm = Llama(
    model_path=str(MODEL_PATH),
    n_ctx=N_CTX,
    n_threads=N_THREADS,
    n_batch=N_BATCH,
    verbose=False,
)

history = [{"role": "system", "content": SYSTEM_PROMPT}]

print("\nCLI chatbot ready. Type 'exit' or 'quit' to leave.\n")

while True:
    try:
        user = input("you › ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nbye! ")
        break

    if user.lower() in {"exit", "quit"}:
        print("bye! ")
        break

    history.append({"role": "user", "content": user})

    stream = llm.create_chat_completion(
        messages=history,
        stream=True,
        temperature=0.7,
        top_p=0.95,
        max_tokens=512,
    )

    print("bot › ", end="", flush=True)
    assistant_reply = []
    for chunk in stream:
        token = chunk["choices"][0]["delta"].get("content", "")
        if token:
            assistant_reply.append(token)
            print(token, end="", flush=True)
    print()  # newline
    history.append({"role": "assistant", "content": "".join(assistant_reply)})
