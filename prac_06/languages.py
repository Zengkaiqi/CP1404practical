"""
language
Estimate: 10 minutes
Actual:   11 minutes
"""
from prac_06.programming_language import ProgrammingLanguage
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)
print("The dynamically typed languages are:")
language = [python,ruby,visual_basic]
for language in language:
    if language.is_dynamic():
        print(language.name)
