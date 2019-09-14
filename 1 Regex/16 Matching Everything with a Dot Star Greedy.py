# dot star uses greedy mode
import re

regexObj = re.compile(r"First Name:(.*) Last Name:(.*)")
matchTuple = regexObj.findall("First Name:Mayank Last Name:Singh")
print(matchTuple)
