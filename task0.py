def fizzbuzz(max_num=101):
	for i in range(max_num):
	    print(i)
            value = ""
            if i % 3 == 0: value +="fizz"
	    if i % 5 == 0: value +="buzz"
            yield value if value else i


for number, burp in enumerate(fizzbuzz()):
    print "%s: %s" % (number, burp)
