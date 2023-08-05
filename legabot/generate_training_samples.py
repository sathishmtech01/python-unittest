# import yaml
# data = [{"id":"1","questions":["What is bankruptcy","tell me about bankruptcy"],"answer":"Bankruptcy is a legal process through which people or other entities who cannot repay debts to creditors may seek relief from some or all of their debts"},
#         {"id":"2","questions":["What is litigation?"],"answer":"The process of taking legal action in a court of law"}]
#
nlu = "data/nlu.yml"
stories = "data/stories.yml"
domain = "domain.yml"
prefix = "legal_"
#
# def load_yaml(path):
#         data = yaml.safe_load(open(path, "r",encoding="utf-8"))
#         return data
# def write_yaml(path,file):
#         yaml.dump(file,open(path, "w"),allow_unicode=True)
#         return "saved"
#
# nlu_data = load_yaml(nlu)
# print(load_yaml(nlu))
#
# for val in data:
#         id = prefix+val["id"]
#         questions = val["questions"]
#         answer = val["answer"]
#         nlu_intent = {"intent":id,"examples":""}
#         for q in questions:
#                 nlu_intent["examples"]=nlu_intent["examples"]+"- "+q+"\n"
#
#         # nlu_data["nlu"].append(nlu_intent)
# print(nlu_data)

# print(write_yaml("sample.yml",nlu_data))


from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.training_data.training_data import TrainingData
a = Message.build(text="hello", intent="greet", example_metadata={"paraphrases": ["hey", "hi"]})
td = TrainingData([a])
print(td.nlu_as_yaml())
from rasa.shared.utils.io import read_yaml,read_yaml_file,write_yaml

data = read_yaml_file(nlu)
print(data)
write_yaml(data,"sample.yml")