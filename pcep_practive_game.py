#!/usr/bin/env python3
"""
PYTHON PCEP PRACTICE GAME
An interactive game to practice Python fundamentals for PCEP certification
"""

import random
import time

class PythonPracticeGame:
    def __init__(self):
        self.score = 0
        self.total_questions = 0
        self.streak = 0
        self.best_streak = 0
        self.topics_covered = []
        self.wrong_answers = []
        
    def clear_screen(self):
        """Clear screen for better readability"""
        print("\n" * 2)
        
    def display_header(self):
        """Display game header with current stats"""
        print("=" * 60)
        print("🐍 PYTHON PCEP PRACTICE GAME 🐍".center(60))
        print("=" * 60)
        print(f"Score: {self.score}/{self.total_questions} | Streak: {self.streak} | Best: {self.best_streak}")
        print("-" * 60)
        
    def get_random_question(self):
        """Returns a random question from different categories"""
        categories = [
            self.data_types_question,
            self.operators_question,
            self.list_methods_question,
            self.string_methods_question,
            self.control_flow_question,
            self.dictionary_question,
            self.tuple_question,
            self.type_conversion_question,
            self.indexing_question,
            self.boolean_question,
            self.function_question,
            self.exception_question
        ]
        return random.choice(categories)()
    
    def check_answer(self, user_answer, correct_answer, case_sensitive=False):
        """Check if answer is correct"""
        if not case_sensitive:
            return str(user_answer).strip().lower() == str(correct_answer).strip().lower()
        return str(user_answer).strip() == str(correct_answer).strip()
    
    def data_types_question(self):
        """Questions about Python data types"""
        questions = [
            {
                "question": "What is the type of: 42",
                "answer": "int",
                "hint": "Whole number type"
            },
            {
                "question": "What is the type of: 3.14",
                "answer": "float",
                "hint": "Decimal number type"
            },
            {
                "question": "What is the type of: 'Hello'",
                "answer": "str",
                "hint": "Text type (3 letters)"
            },
            {
                "question": "What is the type of: True",
                "answer": "bool",
                "hint": "True/False type"
            },
            {
                "question": "What is the type of: [1, 2, 3]",
                "answer": "list",
                "hint": "Mutable sequence with square brackets"
            },
            {
                "question": "What is the type of: (1, 2, 3)",
                "answer": "tuple",
                "hint": "Immutable sequence with parentheses"
            },
            {
                "question": "What is the type of: {'a': 1, 'b': 2}",
                "answer": "dict",
                "hint": "Key-value pairs"
            },
            {
                "question": "What is the type of: {1, 2, 3}",
                "answer": "set",
                "hint": "Unique unordered collection"
            },
            {
                "question": "What is the type of: None",
                "answer": "NoneType",
                "hint": "Special null type"
            }
        ]
        return random.choice(questions)
    
    def operators_question(self):
        """Questions about Python operators"""
        a, b = random.randint(1, 10), random.randint(1, 10)
        operations = [
            {"q": f"What is {a} + {b}?", "a": str(a + b)},
            {"q": f"What is {a} * {b}?", "a": str(a * b)},
            {"q": f"What is {a} ** 2?", "a": str(a ** 2)},
            {"q": f"What is {a} // {b}?", "a": str(a // b)},
            {"q": f"What is {a} % {b}?", "a": str(a % b)},
            {"q": f"What is {a} == {b}? (True/False)", "a": str(a == b)},
            {"q": f"What is {a} != {b}? (True/False)", "a": str(a != b)},
            {"q": f"What is {a} > {b}? (True/False)", "a": str(a > b)},
            {"q": f"What is {a} <= {b}? (True/False)", "a": str(a <= b)}
        ]
        op = random.choice(operations)
        return {"question": op["q"], "answer": op["a"], "hint": "Calculate the result"}
    
    def list_methods_question(self):
        """Questions about list methods"""
        questions = [
            {
                "question": "nums = [1, 2, 3]\nnums.append(4)\nWhat is nums now?",
                "answer": "[1, 2, 3, 4]",
                "hint": "append adds to the end"
            },
            {
                "question": "nums = [3, 1, 2]\nnums.sort()\nWhat is nums now?",
                "answer": "[1, 2, 3]",
                "hint": "sort arranges in ascending order"
            },
            {
                "question": "nums = [1, 2, 3]\nnums.pop()\nWhat does pop() return?",
                "answer": "3",
                "hint": "pop() removes and returns the last element"
            },
            {
                "question": "nums = [1, 2, 3, 2]\nWhat is nums.count(2)?",
                "answer": "2",
                "hint": "count() returns number of occurrences"
            },
            {
                "question": "nums = [1, 2, 3]\nWhat is len(nums)?",
                "answer": "3",
                "hint": "len() returns the number of elements"
            },
            {
                "question": "nums = [1, 2, 3]\nnums.insert(0, 0)\nWhat is nums now?",
                "answer": "[0, 1, 2, 3]",
                "hint": "insert(index, value) adds at specific position"
            },
            {
                "question": "nums = [1, 2, 2, 3]\nnums.remove(2)\nWhat is nums now?",
                "answer": "[1, 2, 3]",
                "hint": "remove() deletes first occurrence only"
            },
            {
                "question": "nums = [1, 2, 3]\nnums.reverse()\nWhat is nums now?",
                "answer": "[3, 2, 1]",
                "hint": "reverse() reverses in place"
            }
        ]
        return random.choice(questions)
    
    def string_methods_question(self):
        """Questions about string methods"""
        questions = [
            {
                "question": 'text = "hello"\nWhat is text.upper()?',
                "answer": "HELLO",
                "hint": "Converts to uppercase"
            },
            {
                "question": 'text = "HELLO"\nWhat is text.lower()?',
                "answer": "hello",
                "hint": "Converts to lowercase"
            },
            {
                "question": 'text = "a,b,c"\nWhat is text.split(",")?',
                "answer": "['a', 'b', 'c']",
                "hint": "Returns a list of substrings"
            },
            {
                "question": 'What is "-".join(["a", "b", "c"])?',
                "answer": "a-b-c",
                "hint": "Joins list elements with separator"
            },
            {
                "question": 'text = "hello world"\nWhat is text.replace("world", "python")?',
                "answer": "hello python",
                "hint": "Replaces substring"
            },
            {
                "question": 'text = "  hello  "\nWhat is text.strip()?',
                "answer": "hello",
                "hint": "Removes whitespace from both ends"
            },
            {
                "question": 'text = "Python"\nWhat is text.startswith("Py")?',
                "answer": "True",
                "hint": "Checks if string starts with substring"
            },
            {
                "question": 'text = "Python"\nWhat is text.endswith("on")?',
                "answer": "True",
                "hint": "Checks if string ends with substring"
            }
        ]
        return random.choice(questions)
    
    def control_flow_question(self):
        """Questions about control flow"""
        questions = [
            {
                "question": "for i in range(3):\nWhat values will i have? (comma-separated)",
                "answer": "0, 1, 2",
                "hint": "range(3) starts at 0"
            },
            {
                "question": "for i in range(2, 5):\nWhat values will i have? (comma-separated)",
                "answer": "2, 3, 4",
                "hint": "range(start, stop) - stop is exclusive"
            },
            {
                "question": "x = 5\nif x > 3:\n    result = 'A'\nelse:\n    result = 'B'\nWhat is result?",
                "answer": "A",
                "hint": "Check the condition: is 5 > 3?"
            },
            {
                "question": "count = 0\nwhile count < 2:\n    count += 1\nWhat is final count?",
                "answer": "2",
                "hint": "Loop continues while count < 2"
            },
            {
                "question": "What keyword skips the current iteration in a loop?",
                "answer": "continue",
                "hint": "Not break, but c..."
            },
            {
                "question": "What keyword exits a loop completely?",
                "answer": "break",
                "hint": "Stops the loop immediately"
            },
            {
                "question": "score = 75\nif score >= 90:\n    grade = 'A'\nelif score >= 70:\n    grade = 'B'\nelse:\n    grade = 'C'\nWhat is grade?",
                "answer": "B",
                "hint": "75 is >= 70 but < 90"
            }
        ]
        return random.choice(questions)
    
    def dictionary_question(self):
        """Questions about dictionaries"""
        questions = [
            {
                "question": 'd = {"a": 1, "b": 2}\nWhat is d["a"]?',
                "answer": "1",
                "hint": "Access value by key"
            },
            {
                "question": 'd = {"a": 1}\nd["b"] = 2\nHow many keys does d have now?',
                "answer": "2",
                "hint": "Adding a new key-value pair"
            },
            {
                "question": 'd = {"a": 1, "b": 2}\nWhat does list(d.keys()) return?',
                "answer": "['a', 'b']",
                "hint": "Returns list of all keys"
            },
            {
                "question": 'd = {"a": 1}\nWhat is d.get("b", 0)?',
                "answer": "0",
                "hint": "get() returns default if key not found"
            },
            {
                "question": 'd = {"a": 1, "b": 2, "c": 3}\nWhat is len(d)?',
                "answer": "3",
                "hint": "Number of key-value pairs"
            },
            {
                "question": 'd = {"a": 1, "b": 2}\n"a" in d returns what?',
                "answer": "True",
                "hint": "Checks if key exists"
            },
            {
                "question": 'd = {"a": 1}\nd.pop("a")\nWhat does pop() return?',
                "answer": "1",
                "hint": "pop() removes and returns the value"
            }
        ]
        return random.choice(questions)
    
    def tuple_question(self):
        """Questions about tuples"""
        questions = [
            {
                "question": "t = (1, 2, 3)\nCan you do t[0] = 5? (yes/no)",
                "answer": "no",
                "hint": "Tuples are immutable"
            },
            {
                "question": "t = (1, 2, 3, 2)\nWhat is t.count(2)?",
                "answer": "2",
                "hint": "count() works on tuples too"
            },
            {
                "question": "t = (10,)\nWhat type is t?",
                "answer": "tuple",
                "hint": "Single element tuple needs comma"
            },
            {
                "question": "x, y = (5, 10)\nWhat is x?",
                "answer": "5",
                "hint": "Tuple unpacking"
            },
            {
                "question": "t = (1, 2, 3)\nWhat is t[1]?",
                "answer": "2",
                "hint": "Access by index (0-based)"
            },
            {
                "question": "t = (1, 2, 3)\nWhat is len(t)?",
                "answer": "3",
                "hint": "Number of elements"
            },
            {
                "question": "What's the difference between (10) and (10,)?",
                "answer": "(10) is int, (10,) is tuple",
                "hint": "Comma makes it a tuple"
            }
        ]
        return random.choice(questions)
    
    def type_conversion_question(self):
        """Questions about type conversion"""
        questions = [
            {
                "question": 'int("42") returns what?',
                "answer": "42",
                "hint": "String to integer"
            },
            {
                "question": 'str(100) returns what?',
                "answer": "100",
                "hint": "Integer to string (keep the value)"
            },
            {
                "question": 'list("abc") returns what?',
                "answer": "['a', 'b', 'c']",
                "hint": "Each character becomes an element"
            },
            {
                "question": 'float("3.14") returns what?',
                "answer": "3.14",
                "hint": "String to decimal number"
            },
            {
                "question": 'bool(0) returns what?',
                "answer": "False",
                "hint": "0 is considered False"
            },
            {
                "question": 'bool(1) returns what?',
                "answer": "True",
                "hint": "Non-zero is True"
            },
            {
                "question": 'bool([]) returns what?',
                "answer": "False",
                "hint": "Empty containers are False"
            },
            {
                "question": 'list((1, 2, 3)) returns what?',
                "answer": "[1, 2, 3]",
                "hint": "Tuple to list conversion"
            },
            {
                "question": 'tuple([1, 2, 3]) returns what?',
                "answer": "(1, 2, 3)",
                "hint": "List to tuple conversion"
            }
        ]
        return random.choice(questions)
    
    def indexing_question(self):
        """Questions about indexing and slicing"""
        questions = [
            {
                "question": 'text = "Python"\nWhat is text[0]?',
                "answer": "P",
                "hint": "First character (index 0)"
            },
            {
                "question": 'text = "Python"\nWhat is text[-1]?',
                "answer": "n",
                "hint": "Last character"
            },
            {
                "question": 'text = "Python"\nWhat is text[1:4]?',
                "answer": "yth",
                "hint": "From index 1 up to (not including) 4"
            },
            {
                "question": 'nums = [10, 20, 30]\nWhat is nums[1]?',
                "answer": "20",
                "hint": "Second element (index 1)"
            },
            {
                "question": 'nums = [1, 2, 3, 4, 5]\nWhat is nums[::2]?',
                "answer": "[1, 3, 5]",
                "hint": "Every second element"
            },
            {
                "question": 'text = "Hello"\nWhat is text[:3]?',
                "answer": "Hel",
                "hint": "From start up to index 3"
            },
            {
                "question": 'text = "Hello"\nWhat is text[2:]?',
                "answer": "llo",
                "hint": "From index 2 to end"
            },
            {
                "question": 'nums = [0, 1, 2, 3, 4]\nWhat is nums[-2]?',
                "answer": "3",
                "hint": "Second from the end"
            }
        ]
        return random.choice(questions)
    
    def boolean_question(self):
        """Questions about boolean logic"""
        questions = [
            {
                "question": "True and False returns what?",
                "answer": "False",
                "hint": "and needs both to be True"
            },
            {
                "question": "True or False returns what?",
                "answer": "True",
                "hint": "or needs at least one True"
            },
            {
                "question": "not True returns what?",
                "answer": "False",
                "hint": "not reverses the boolean"
            },
            {
                "question": "5 > 3 and 2 < 4 returns what?",
                "answer": "True",
                "hint": "Both conditions are True"
            },
            {
                "question": "[] is an empty list. bool([]) returns what?",
                "answer": "False",
                "hint": "Empty containers are False"
            },
            {
                "question": "What is 10 > 5 > 1?",
                "answer": "True",
                "hint": "Chain comparison: 10 > 5 AND 5 > 1"
            },
            {
                "question": "not False returns what?",
                "answer": "True",
                "hint": "not reverses the boolean"
            }
        ]
        return random.choice(questions)
    
    def function_question(self):
        """Questions about functions"""
        questions = [
            {
                "question": "def greet(name):\n    return 'Hello ' + name\n\nWhat is greet('Alice')?",
                "answer": "Hello Alice",
                "hint": "Function concatenates strings"
            },
            {
                "question": "def add(a, b=5):\n    return a + b\n\nWhat is add(3)?",
                "answer": "8",
                "hint": "b has default value 5"
            },
            {
                "question": "def multiply(x, y):\n    return x * y\n\nWhat is multiply(4, 3)?",
                "answer": "12",
                "hint": "4 times 3"
            },
            {
                "question": "What keyword defines a function?",
                "answer": "def",
                "hint": "Three letters, starts with d"
            },
            {
                "question": "What keyword sends a value back from a function?",
                "answer": "return",
                "hint": "Sends value back to caller"
            },
            {
                "question": "def test():\n    pass\n\nWhat does test() return?",
                "answer": "None",
                "hint": "Functions without return statement return None"
            }
        ]
        return random.choice(questions)
    
    def exception_question(self):
        """Questions about exceptions and errors"""
        questions = [
            {
                "question": "What error: print(undefined_variable)?",
                "answer": "NameError",
                "hint": "Variable name not defined"
            },
            {
                "question": "What error: 10 / 0?",
                "answer": "ZeroDivisionError",
                "hint": "Cannot divide by zero"
            },
            {
                "question": "What error: [1, 2, 3][10]?",
                "answer": "IndexError",
                "hint": "Index out of range"
            },
            {
                "question": "What error: {'a': 1}['b']?",
                "answer": "KeyError",
                "hint": "Dictionary key not found"
            },
            {
                "question": "What error: '2' + 2?",
                "answer": "TypeError",
                "hint": "Cannot add string and integer"
            },
            {
                "question": "What error: int('hello')?",
                "answer": "ValueError",
                "hint": "Invalid value for conversion"
            }
        ]
        return random.choice(questions)
    
    def play_round(self):
        """Play one round of the game"""
        self.clear_screen()
        self.display_header()
        
        # Get a random question
        q_data = self.get_random_question()
        
        print(f"\n📝 QUESTION {self.total_questions + 1}:")
        print("-" * 40)
        print(q_data["question"])
        print("-" * 40)
        
        # Get user answer
        user_answer = input("\nYour answer: ")
        
        # Check for quit command
        if user_answer.lower() in ['quit', 'exit', 'q']:
            return False
        
        # Check answer
        if self.check_answer(user_answer, q_data["answer"]):
            print("✅ CORRECT!")
            self.score += 1
            self.streak += 1
            if self.streak > self.best_streak:
                self.best_streak = self.streak
            if self.streak >= 3:
                print(f"🔥 {self.streak} in a row! Keep it up!")
        else:
            print(f"❌ INCORRECT!")
            print(f"Correct answer: {q_data['answer']}")
            print(f"💡 Hint: {q_data['hint']}")
            self.wrong_answers.append({
                "question": q_data["question"],
                "your_answer": user_answer,
                "correct_answer": q_data["answer"]
            })
            self.streak = 0
        
        self.total_questions += 1
        
        # Show current score
        accuracy = (self.score / self.total_questions) * 100
        print(f"\n📊 Current accuracy: {accuracy:.1f}%")
        return True
        
    def show_menu(self):
        """Display game menu"""
        self.clear_screen()
        self.display_header()
        print("\n🎮 GAME MODES:")
        print("1. Quick Practice (5 questions)")
        print("2. Standard Practice (10 questions)")
        print("3. Marathon (20 questions)")
        print("4. Endless Mode")
        print("5. View Tips")
        print("6. Review Mistakes")
        print("7. Exit")
        return input("\nChoose mode (1-7): ")
    
    def show_tips(self):
        """Display PCEP study tips"""
        self.clear_screen()
        print("=" * 60)
        print("📚 PCEP EXAM TIPS".center(60))
        print("=" * 60)
        tips = """
        KEY CONCEPTS TO MASTER:
        
        1. DATA TYPES: 
           - int, float, str, bool, list, tuple, dict, set
           - Know type() function
        
        2. OPERATORS:
           - Arithmetic: +, -, *, /, //, %, **
           - Comparison: ==, !=, <, >, <=, >=
           - Logical: and, or, not
           
        3. STRINGS:
           - Methods: upper(), lower(), split(), join(), replace()
           - Slicing: text[start:stop:step]
           
        4. LISTS:
           - Methods: append(), insert(), remove(), pop(), sort()
           - Mutable (can be changed)
           
        5. TUPLES:
           - Immutable (cannot be changed)
           - Single element needs comma: (10,)
           
        6. DICTIONARIES:
           - Key-value pairs
           - Methods: get(), keys(), values(), items()
           
        7. CONTROL FLOW:
           - if/elif/else
           - for loops with range()
           - while loops
           - break and continue
           
        8. FUNCTIONS:
           - def keyword
           - return statement
           - Default parameters
           
        9. EXCEPTIONS:
           - NameError, TypeError, ValueError
           - IndexError, KeyError, ZeroDivisionError
           
        10. TYPE CONVERSION:
            - int(), float(), str(), list(), tuple(), bool()
        
        REMEMBER:
        - Indexing starts at 0
        - Negative indices count from the end
        - Empty containers are False in boolean context
        - None is returned if function has no return statement
        """
        print(tips)
        input("\nPress Enter to continue...")
    
    def review_mistakes(self):
        """Review wrong answers from current session"""
        self.clear_screen()
        print("=" * 60)
        print("📝 REVIEW YOUR MISTAKES".center(60))
        print("=" * 60)
        
        if not self.wrong_answers:
            print("\n✨ No mistakes yet! Keep practicing!")
        else:
            print(f"\nYou had {len(self.wrong_answers)} mistake(s):\n")
            for i, mistake in enumerate(self.wrong_answers, 1):
                print(f"{i}. Question: {mistake['question']}")
                print(f"   Your answer: {mistake['your_answer']}")
                print(f"   Correct answer: {mistake['correct_answer']}")
                print("-" * 40)
        
        input("\nPress Enter to continue...")
    
    def play_game(self, num_questions=None):
        """Main game loop"""
        self.score = 0
        self.total_questions = 0
        self.streak = 0
        
        if num_questions:
            print(f"\n🎯 Goal: {num_questions} questions")
            print("💡 Type 'quit' to exit early")
            time.sleep(2)
            
            for i in range(num_questions):
                if not self.play_round():
                    print("\n👋 Exiting game...")
                    break
                if i < num_questions - 1:
                    input("\nPress Enter for next question...")
        else:
            # Endless mode
            print("\n♾️ ENDLESS MODE - Type 'quit' to exit")
            time.sleep(2)
            while True:
                if not self.play_round():
                    print("\n👋 Exiting endless mode...")
                    break
                input("\nPress Enter for next question...")
        
        # Show final score
        if self.total_questions > 0:
            self.show_final_score()
    
    def show_final_score(self):
        """Display final results"""
        self.clear_screen()
        print("=" * 60)
        print("🏆 GAME OVER 🏆".center(60))
        print("=" * 60)
        
        accuracy = (self.score / self.total_questions) * 100
        print(f"\n📊 Final Score: {self.score}/{self.total_questions}")
        print(f"📈 Accuracy: {accuracy:.1f}%")
        print(f"🔥 Best Streak: {self.best_streak}")
        
        # Give feedback based on performance
        if accuracy >= 90:
            print("\n⭐ EXCELLENT! You're ready for PCEP!")
            print("Consider taking practice exams next.")
        elif accuracy >= 70:
            print("\n👍 GOOD JOB! You're getting there!")
            print("Focus on the topics you missed.")
        elif accuracy >= 50:
            print("\n📚 KEEP STUDYING! You're making progress.")
            print("Review the basics and try again.")
        else:
            print("\n💪 DON'T GIVE UP! Everyone starts somewhere.")
            print("Review the tips and practice daily.")
        
        if self.wrong_answers:
            print(f"\n❗ You had {len(self.wrong_answers)} mistake(s)")
            print("Use option 6 to review them.")
        
        input("\nPress Enter to continue...")
    
    def run(self):
        """Run the game"""
        print("=" * 60)
        print("🐍 Welcome to Python PCEP Practice Game! 🐍")
        print("=" * 60)
        print("\nTest your knowledge of Python basics")
        print("Perfect for PCEP certification preparation!")
        time.sleep(2)
        
        while True:
            choice = self.show_menu()
            
            if choice == "1":
                self.play_game(5)
            elif choice == "2":
                self.play_game(10)
            elif choice == "3":
                self.play_game(20)
            elif choice == "4":
                self.play_game(None)
            elif choice == "5":
                self.show_tips()
            elif choice == "6":
                self.review_mistakes()
            elif choice == "7":
                print("\n👋 Thanks for playing!")
                print("Good luck with your PCEP certification! 🎓")
                break
            else:
                print("Invalid choice. Please try again.")
                time.sleep(1)

# Run the game
if __name__ == "__main__":
    game = PythonPracticeGame()
    game.run()

