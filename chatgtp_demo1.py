import openai
import time
import pytest
# import torch.nn as nn



# # 需求一
# def generate_prompt(prompt):
#     # return "请为我翻译后面的语句或单词为罗马文."+prompt
#     return prompt

# def openai_replay(content):
#     openai.api_key = api_key
#     res = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         # model="code-davinci-002",
#         messages=[{"role":"user","content":generate_prompt(content)}],
#         temperature=0.7,
#         max_tokens=1000,
#         top_p=1 
#     )
#     return res.choices[0].message.content

# def common_prefix():
#     a = 10
#     b = 20
#     c = [a,b,a*b,a+b]
#     d = c[:2]
#     print(d)

    


if __name__ == "__main__":  
    # while True:
    #     msg = input("-----请输入..------\n")
    #     reply = openai_replay(str(msg))
    #     print(reply)      
    #     time.sleep(1)
    # openai.organization = "***********************"
    # openai.api_key = "**********************************"
    model_list =  openai.Model.list()
    model_dict = {}
    for k, model in enumerate(model_list.data):
        if ":" in model.root:
            continue
        print(model.root)
        model_dict[k] = model.root 

