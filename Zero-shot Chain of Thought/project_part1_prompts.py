system_message_nus = "You are an AI tutor. You have to help a student learning programming. The program uses Python. You have to strictly follow the format for the final output as instructed below."

user_message_nus_repair_basic = """
Following is the setup of a problem in Python. It contains the description and a sample testcase.

[Problem Starts]
{problem_data}
[Problem Ends]

Following is the student's buggy code for this problem:

[Buggy Code Starts]
{buggy_program}
[Buggy Code Ends]


Fix the buggy code. Output your entire fixed code between [FIXED] and [/FIXED].
"""

user_message_nus_hint_basic = """
Following is the setup of a problem in Python. It contains the description and a sample testcase.

[Problem Starts]
{problem_data}
[Problem Ends]

Following is the student's buggy code for this problem:

[Buggy Code Starts]
{buggy_program}
[Buggy Code Ends]

Provide a concise single-sentence hint to the student about one bug in the student's buggy code. Output your hint between [HINT] and [/HINT].
"""

user_message_nus_explanation_basic = """ 
Following is the setup of a problem in Python. It contains the description and a sample testcase.

[Problem Starts]
{problem_data}
[Problem Ends]

Following is the student's buggy code for this problem:

[Buggy Code Starts]
{buggy_program}
[Buggy Code Ends]

Following is the repaired code:

[Repaired Code Starts]
{repaired_program}
[Repaired Code Ends]

1) Provide a detailed and a step-by-step explaination of the bug(s) in the student's buggy code and the required fixes.
2) Based on your explanation of the bug(s) and the required fixes, provide a concise single-sentence hint to the student about one bug in the student's buggy code. The hint should not be too detailed as the student should be made to think about the fix themselves. However, the hint should not be too abstract as the student is stuck and needs help. Output your hint strictly between [HINT] and [/HINT].

"""