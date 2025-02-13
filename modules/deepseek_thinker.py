import ollama
from pathlib import Path

def enviar_ia(prompt:str, ruta_texto:Path):
    directrices = """You are an expert in providing documentation on programming-related topics.
The documentation you provide should help you understand the requested topic correctly.
You think in English and respond in Spanish using Markdown formatting, focusing on readability for python markdown."""

    # Enviamos el promt a la IA
    response = ollama.chat(
        model="deepseek-r1:7b",
        messages=[
            {"role":"system", "content":directrices},
            {"role":"user", "content":f"Dame documentación sobre: {prompt}"}
        ]
    )

    # Respuesta de la IA
    analysis:str = response["message"]["content"]
    analysis_list:list = analysis.split("\n")
    post_think:bool = False
    post_br:bool = False
    with open(ruta_texto, "w", encoding="utf-8") as file:
        for line in analysis_list:
            if post_think == True and line != "\n":
                post_br = True
            if line == "</think>":
                post_think = True
            if post_think == True and post_br == True:
                line+="\n"
                file.write(line)
