# Regular Expression Symbols

1. ()? matches zero or one of the preceding groups
2. * matches 0 or more of the preceding groups
3. + matches 1 or more of the preceding groups
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
20. 
