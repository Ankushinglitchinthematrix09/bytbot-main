from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

class ChatBotCore:
    def __init__(self):
        self.bot = ChatBot(
            'BytBot',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            logic_adapters=[
                'chatterbot.logic.BestMatch',
                'chatterbot.logic.MathematicalEvaluation'
            ]
        )
        self.trainer = ChatterBotCorpusTrainer(self.bot)
        
    def train_bot(self):
        # Train with basic corpus data
        self.trainer.train("chatterbot.corpus.english.greetings",
                         "chatterbot.corpus.english.conversations")
        
        # Add custom training data
        list_trainer = ListTrainer(self.bot)
        list_trainer.train([
            "Hi",
            "Hello! How can I help you today?",
            "What can you do?",
            "I can help answer questions and have conversations with you!",
            "Bye",
            "Goodbye! Have a great day!"
        ])
    
    def get_response(self, user_input):
        try:
            response = self.bot.get_response(user_input)
            return str(response)
        except Exception as e:
            return "I'm sorry, I'm having trouble understanding that."
