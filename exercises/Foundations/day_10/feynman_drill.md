# Least understand concept - counting_02.py
`In this part the exercise asks about how many total possible outcomes for certain conditions.  Password rules: 8 chars, uppercase + lowercase + digits (62 chars). (a) Total possible? (b) Must contain at least one digit? (use complement: total − no digits). (c) Must contain at least one of each type? (inclusion-exclusion over 3 types).`

`Imagine you are making an 8-character secret code using letters and numbers.
There are three rules:
You need at least one small letter, like a.
You need at least one BIG letter, like A.
You need at least one number, like 5.
First, imagine putting every possible code into one giant pile. Some of these codes will follow all the rules, but some will not.
Now, we take out the bad codes. We remove codes that have no numbers, codes that have no BIG letters, and codes that have no small letters.
But wait! Some codes get removed twice.
For example, abcdefgh has no BIG letters and no numbers. So it gets removed when we take out codes with no BIG letters, and then it gets removed again when we take out codes with no numbers.
We only wanted to remove it once, so we put it back once.
We do the same thing for codes made of only BIG letters or only numbers.
After fixing these mistakes, the codes left in the pile follow all three rules.
`