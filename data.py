# question_data = [
# 	{"text": "A slug's blood is green.", "answer": "True"},
# 	{"text": "The loudest animal is the African Elephant.", "answer": "False"},
# 	{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
# 	{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
# 	{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, "
# 	         "you are free to take it home to eat.", "answer": "True"},
# 	{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
# 	          "answer": "False"},
# 	{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
# 	{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
# 	{"text": "Google was originally called 'Backrub'.", "answer": "True"},
# 	{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
# 	{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
# 	{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]


# computer quiz ( first 10 : easy leve, then 10 medium level)



"""

https://opentdb.com

https://opentdb.com/api_config.php
"""
question_data = [
	
	{"category": "Science: Computers",
	 "type": "boolean",
	 "difficulty": "easy",
	 "question": "Linus Torvalds created Linux and Git.",
	 "correct_answer": "True",
	 "incorrect_answers": ["False"]},
	
	{"category": "Science: Computers",
	 "type": "boolean",
	 "difficulty": "easy",
	 "question": "The programming language &quot;Python&quot; is based off a modified version of &quot;JavaScript&quot;.",
	 "correct_answer": "False",
	 "incorrect_answers": ["True"]},
	
	{"category": "Science: Computers",
	 "type": "boolean", "difficulty": "easy",
	 "question": "The logo for Snapchat is a Bell.",
	 "correct_answer": "False",
	 "incorrect_answers": ["True"]},
	
	{"category": "Science: Computers",
	 "type": "boolean", "difficulty": "easy",
	 "question": "Pointers were not used in the original C programming language; they were added later on in C++.",
	 "correct_answer": "False",
	 "incorrect_answers": ["True"]},
	
	{"category": "Science: Computers",
	 "type": "boolean",
	 "difficulty": "easy",
	 "question": "Ada Lovelace is often considered the first computer programmer.",
	 "correct_answer": "True",
	 "incorrect_answers": ["False"]},
	
	{"category": "Science: Computers",
	 "type": "boolean",
	 "difficulty": "easy",
	 "question": "&quot;HTML&quot; stands for Hypertext Markup Language.",
	 "correct_answer": "True", "incorrect_answers": ["False"]},
	
	{"category": "Science: Computers",
	 "type": "boolean",
	 "difficulty": "easy",
	 "question": "In most programming languages, the operator ++ is equivalent to the statement &quot;+= 1&quot;.",
	 "correct_answer": "True", "incorrect_answers": ["False"]},
	
	{"category": "Science: Computers",
	 "type": "boolean",
	 "difficulty": "easy",
	 "question": "The Windows 7 operating system has six main editions.", "correct_answer": "True",
	 "incorrect_answers": ["False"]},
	
	{"category": "Science: Computers",
	 "type": "boolean",
	 "difficulty": "easy",
	 "question": "The Windows ME operating system was released in the year 2000.",
	 "correct_answer": "True",
	 "incorrect_answers": ["False"]},
	
	{"category": "Science: Computers",
	 "type": "boolean",
	 "difficulty": "easy",
	 "question": "The Python programming language gets its name from the British comedy group &quot;Monty Python.&quot;",
	 "correct_answer": "True", "incorrect_answers": ["False"]},
	{"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
	 "question": "The common software-programming acronym &quot;I18N&quot; comes from the term &quot;Interlocalization&quot;.",
	 "correct_answer": "False", "incorrect_answers": ["True"]},
	{"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
	 "question": "FLAC stands for &quot;Free Lossless Audio Condenser&quot;&#039;", "correct_answer": "False",
	 "incorrect_answers": ["True"]}, {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
	                                  "question": "The very first recorded computer &quot;bug&quot; was a moth found inside a Harvard Mark II computer.",
	                                  "correct_answer": "True", "incorrect_answers": ["False"]},
	{"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
	 "question": "To bypass US Munitions Export Laws, the creator of the PGP published all the source code in book form. ",
	 "correct_answer": "True", "incorrect_answers": ["False"]},
	{"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
	 "question": "MacOS is based on Linux.", "correct_answer": "False", "incorrect_answers": ["True"]},
	{"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
	 "question": "The open source program Redis is a relational database server.", "correct_answer": "False",
	 "incorrect_answers": ["True"]}, {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
	                                  "question": "The first dual-core CPU was the Intel Pentium D.",
	                                  "correct_answer": "False", "incorrect_answers": ["True"]},
	{"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
	 "question": "It&#039;s not possible to format a write-protected DVD-R Hard Disk.", "correct_answer": "True",
	 "incorrect_answers": ["False"]}, {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
	                                   "question": "Android versions are named in alphabetical order.",
	                                   "correct_answer": "True", "incorrect_answers": ["False"]},
	{"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
	 "question": "Linus Sebastian is the creator of the Linux kernel, which went on to be used in Linux, Android, and Chrome OS.",
	 "correct_answer": "False", "incorrect_answers": ["True"]}
]

"""
# Genearal knowlege (medium level)
question_data = [{"category": "General Knowledge", "type": "boolean", "difficulty": "medium",
                  "question": "The sum of all the numbers on a roulette wheel is 666.", "correct_answer": "True",
                  "incorrect_answers": ["False"]},
                 {"category": "General Knowledge", "type": "boolean", "difficulty": "medium",
                  "question": "An eggplant is a vegetable.", "correct_answer": "False", "incorrect_answers": ["True"]},
                 {"category": "General Knowledge", "type": "boolean", "difficulty": "medium",
                  "question": "The bikini is named after the &quot;Bikini Atoll&quot;, an island where the United States conducted tests on atomic bombs.",
                  "correct_answer": "True", "incorrect_answers": ["False"]},
                 {"category": "General Knowledge", "type": "boolean", "difficulty": "medium",
                  "question": "Cucumbers are usually more than 90% water.", "correct_answer": "True",
                  "incorrect_answers": ["False"]},
                 {"category": "General Knowledge", "type": "boolean", "difficulty": "medium",
                  "question": "You are allowed to sell your soul on eBay.", "correct_answer": "False",
                  "incorrect_answers": ["True"]},
                 {"category": "General Knowledge", "type": "boolean", "difficulty": "medium",
                  "question": "The average woman is 5 inches \/ 13 centimeters shorter than the average man.",
                  "correct_answer": "True", "incorrect_answers": ["False"]},
                 {"category": "General Knowledge", "type": "boolean", "difficulty": "medium",
                  "question": "Sitting for more than three hours a day can cut two years off a person&#039;s life expectancy.",
                  "correct_answer": "True", "incorrect_answers": ["False"]},
                 {"category": "General Knowledge", "type": "boolean", "difficulty": "medium",
                  "question": "Albert Einstein had trouble with mathematics when he was in school.",
                  "correct_answer": "False", "incorrect_answers": ["True"]},
                 {"category": "General Knowledge", "type": "boolean", "difficulty": "medium",
                  "question": "Popcorn was invented in 1871 by Frederick W. Rueckheim in the USA where he sold the snack on the streets of Chicago.",
                  "correct_answer": "False", "incorrect_answers": ["True"]},
                 {"category": "General Knowledge", "type": "boolean", "difficulty": "medium",
                  "question": "&quot;Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo.&quot; is a grammatically correct sentence.",
                  "correct_answer": "True", "incorrect_answers": ["False"]}]
                  
"""
