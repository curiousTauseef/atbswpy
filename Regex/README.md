# Regular Expression Symbols

1. ()? matches zero or one of the preceding groups
2. '*' (without quotes) matches 0 or more of the preceding groups
3. '+' (without quotes) matches 1 or more of the preceding groups
4. {n} matches exactly n of the preceding groups
5. {n,} matches n or more of the preceding groups
6. {,m} matches 0 or more utpo m of the preceding groups
7. {n,m} macthes n to m of the matching groups, follows greed approach will return the largest matching result
8. {n,m}? or *? or +? follow the non greedy approach which means will return the shortest matching string
9. ^spam matches the beginning should be spam
10. spam$ matches the trailing section which should be spam
11. . matches any character except newline character
12. \d matches digits, \D macthes anything except digits
13. \w macthes words, \W matches anything except words
14. \s macthes space characters, \S macthes anything excpet space characters
15. [abc] matches characters anything in the square brackets, like here it matches a or b or c
16. [^abc] matches any characters except a or b or c
17. re.DOTALL matches newline characters, in search method
18. re.I or re.IGNORECASE macthes case insensitive results , otherwise regex is specific of casing
19. Regex Objects sub method is used to replace mathed String, it take two argument (substitution,old string), new substituted string will be returned in response
20. re.VERBOSE is used to ignore Whitespaces and Comments inside the Regex Pattern
21. \b to match the boundaries, don't include ^ or $ if matching boundary at beginning or ending
22. '|' without quotes , pipe characters are used to match alternations, | match a single item out of several possible items separated by the vertical bar.
23. Using Escape Sequence for characters is must, \. \, etc.
24. Backrefrencing (\d)\1 should return 00,11,22,33,44,55,66,77,88,99 , refrencing to groups with the help of \1 \2 \3 according to group number
