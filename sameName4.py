def spam():
    print(eggs)  # Error
    eggs = 'spam'


eggs = 'global'
spam()
print(eggs)
