from chatterbot import ChatBot
import os
linkedin = 'https://www.linkedin.com/in/rodcoelho/'
github = 'https://github.com/rodcoelho'
new = 2

from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
chatterbot = ChatBot(
    'RodBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    database='./database.sqlite3',
    filters=["chatterbot.filters.RepetitiveResponseFilter"]
)

# how to train the bot to respond
chatterbot.set_trainer(ListTrainer)
linkedin_list = ['CV', 'Resume', 'cv', 'resume', 'linkedin', 'Linkedin']
github_list = ['Git', 'git', 'github', 'Github', 'projects']

for words in linkedin_list:
    chatterbot.train([words,linkedin])
for words in github_list:
    chatterbot.train([words,github])
chatterbot.train([
    "Who is Rod?",
    "LINK TO ABOUT PAGE"])

chatterbot.set_trainer(ChatterBotCorpusTrainer)
chatterbot.train("chatterbot.corpus.english.greetings")
#chatterbot.train("chatterbot.corpus.english.conversations")

def openwebsite(link):
    os.system('python -mwebbrowser {}'.format(link))

def clearmemory():
    os.system('rm database.sqlite3')
    os.system('clear')



while True:
    try:
        bot_input = chatterbot.get_response(None)
        if bot_input == linkedin:
            openwebsite(linkedin)
        elif bot_input == github:
            openwebsite(github)

    except(KeyboardInterrupt, EOFError, SystemExit):
        clearmemory()
        break
