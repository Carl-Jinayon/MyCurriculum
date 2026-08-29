# My mistakes

- Entry 1 — Conditional fall-through in login_sim (2026-08-19, Day 3)
- Entry 2 — Loop counter off-by-one (2026-08-20, Day 4 guess_game)
- Entry 3 — Return value of mutating methods (2026-08-22, Day 6 mastery check)
- Entry 4 — Inclusion-exclusion sign alternation (2026-08-24, Math Day 3 counting_02)

# Answers
### Entry 1:
`From the mistake log for the entry 1 I have said that 2 seperate if blocks act like a if else ladder. But no, two seperate ifs are independent. Meaning if the first and the second two separate condition that does not rely to one another. They might both became true, unlike a ladder only one will be true.`

### Entry 2
`That time I placed the attempts in the end of the block and the condition that makes the loop stops is on top of it. So that makes it buggy, because if the loop stops using the break statement it never reaches the attempts thus not counting the first attempt incase the user guessed it only in one try.`

### Entry 3
`In this part, this is just a wrong use of word. The list.sort() does not return anything. It implicitly sorts the list. And returns nothing. If you want the sorted list to be returned you might wanna use the sorted(list) method`

### Entry 4
`In this part my problem is not adding those possibilities (those double subtracts) making the it wrong. Those simple mistakes makes the result different from the actual answers. Before having the result I must make good understanding first about those data that is combined and those that should be excluded.`