import itertools
res = itertools.permutations('abcdefghijklmnopqrstuv12345678@*&%^$> ',8) # 3 is the length of your result.
for i in res:
   print ''.join(i)
