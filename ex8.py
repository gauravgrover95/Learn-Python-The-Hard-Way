formatter = "%r %r %r %r"

print ""
print ""
print formatter %(1,2,3,4)
print formatter %("one","two","three","four")
print formatter %(formatter, formatter,formatter, formatter)
print formatter %(
		"hi",
		"my name is",
		"Gaurav",
		"Grover"
	)
