from django.core.management.base import BaseCommand, CommandError
from pravotznpk.models import Subject, Question, Choice
import json

class Command(BaseCommand):
    help = 'Save Tests'

    def handle(self, *args, **options):
        with open('PRAVO.txt', "r", encoding='utf-8') as file:
            file_content = file.read()
        js = json.loads(file_content)
        categories = js["Categories"]
        for i in categories:
            name = i["Name"]
            category = Subject.objects.create(subject_name=name)
            print("Save Subject: {}".format(name))
            tests = i["Test"]
            for test in tests:
                test_question = test["Question"]
                question = category.question_set.create(question_text=test_question)
                print("Save Question ----------")
                answers = test["Answers"]
                for answer in answers:
                    answer_text = answer["Answer"]
                    iscorrect = answer["IsCorrect"]
                    choice = Choice(choice_text=answer_text, is_correct=iscorrect)
                    question.choice_set.add(choice, bulk=False)
                    print("Save Choice")

        print("Done!!!")



            
        
