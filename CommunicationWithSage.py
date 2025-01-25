import ollama
from string import Template

def generate_response(system_message, user_prompt):

    template = """{{ if .System }}<|im_start|>system
    {{ .System }}<|im_end|>
    {{ end }}{{ if .Prompt }}<|im_start|>user
    {{ .Prompt }}<|im_end|>
    {{ end }}<|im_start|>assistant"""

    
    template = template.replace("{{ .System }}", "${System}")
    template = template.replace("{{ .Prompt }}", "${Prompt}")
    template = template.replace("{{ .Response }}", "${Response}")

    
    variables = {
        "System": system_message,
        "Prompt": user_prompt,
        "Response": ""  
    }

    
    filled_template = Template(template).substitute(variables)

    client = ollama.Client()

    response = client.generate(model="sage", prompt=filled_template)


    return response.response
