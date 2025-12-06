import os

folders = [
    "src",
    "src/agents",
    "src/api",
]

files = {
    "main.py": "",
    "requirements.txt": "",
    "Dockerfile": "",
    "src/__init__.py": "",
    "src/agents/__init__.py": "",
    "src/api/__init__.py": "",

    # Agents
    "src/agents/llm_client.py": "",
    "src/agents/translator_agent.py": "",
    "src/agents/validator_agent.py": "",
    "src/agents/optimizer_agent.py": "",

    # API
    "src/api/server.py": "",
}

print("\n📁 Creating project structure...\n")

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created folder: {folder}")

# Create files
for filepath, content in files.items():
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created file: {filepath}")

print("\n✅ Project structure created successfully!")
