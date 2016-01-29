class Employee(object):

    def hello_python(self, string):

        if string == "print my name":
            print "Gaurav is your name, I suppose. (y/n):"
            response = raw_input("> ")

            if  response == "y":
                print "Welcome Gaurav. Happy to have you here. :)"


            elif response == "n":
                print "Sorry, I dont recognize you"
                print "Please share your name with us?"
                name = raw_input("> ")
                print "Hi " + name + ". Happy to have you here. :)"
      
            else:
                     print "Sorry your response is not known to us"
                     print "Good Bye!"
                     exit(1)
        else:
        	exit(0)

a = Employee()

a.hello_python("print my name")