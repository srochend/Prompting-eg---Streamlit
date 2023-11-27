import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def overview(content):
    prompt = open("overview_prompt.txt").read()
    messages = [{"role":"system", "content": prompt}]

    messages.append({"role":"user", "content":content})
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages)

    response = completion.choices[0].message.content

    with open('overview.txt', 'w') as f:
        f.write(response)

    return response

def standards(content):
    prompt = open("standards_prompt.txt").read()
    messages = [{"role":"system", "content": prompt}]

    messages.append({"role":"user", "content":content})
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages)

    response = completion.choices[0].message.content

    return response

def breakdown(content):
    prompt = open("breakdown_prompt.txt").read()
    messages = [{"role":"system", "content": prompt}]

    messages.append({"role":"user", "content":content})
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages)

    response = completion.choices[0].message.content

    return response

def vocab(content):
    prompt = open("vocab_prompt.txt").read()
    messages = [{"role":"system", "content": prompt}]

    messages.append({"role":"user", "content":content})
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages)

    response = completion.choices[0].message.content

    return response

def assess(content):
    prompt = open("assess_prompt.txt").read()
    messages = [{"role":"system", "content": prompt}]

    messages.append({"role":"user", "content":content})
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages)

    response = completion.choices[0].message.content

    return response