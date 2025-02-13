import ollama

directrices = """
You are an expert in providing documentation on programming-related topics.
The documentation you provide should help you understand the requested topic correctly.
You think in English and respond in Spanish using Markdown format."""

prompt_input = "Bases de datos en python"

# Enviamos el promt a la IA
response = ollama.chat(
    model="deepseek-r1:7b",
    messages=[
        {"role":"system", "content":directrices},
        {"role":"user", "content":f"Dame documentación sobre: {prompt_input}"}
    ]
)

# Imprimimos la respuesta de la IA
analysis:str = response["message"]["content"]
analysis_list:list = analysis.split("\n")
post_think:bool = False
post_br:bool = False
for line in analysis_list:
    if post_think == True and line != "\n":
        post_br = True
    if line == "</think>":
        post_think = True
    if post_think == True and post_br == True:
        print(line)






