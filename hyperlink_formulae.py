
'''
Generating Excel formulae to link cells to another sheet in the file
Kathy Do 09/27/19
'''
for i in range(139):
	j = i + 2
	hyperlink = "=HYPERLINK(\"#groupid_{:d}!A1\",A{:d})".format(i,j)
	print(hyperlink)
	