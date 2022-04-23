text = input("Enter the text:\n ")

if("make money" in text):
	spam = True
elif("buy now" in text):
	spam = True
elif ("click here" in text):
	spam = True
elif("subscribe now" in text):
	spam = True
else:
	spam = False

if(spam):
	print("SPAM - beware")
else:
	print("Great!")