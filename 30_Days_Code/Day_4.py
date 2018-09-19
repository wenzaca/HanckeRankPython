class Person:
    initialAge = int
    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            initialAge = 0

        self.initialAge = initialAge

    def amIOld(self):
        if int(self.initialAge) < 13:
            print("You are young.")
        elif int(self.initialAge) < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        self.initialAge += 1