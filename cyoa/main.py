page_num = 0

while True:
    # open the current page
    file_name = "page " + str(page_num) + ".txt"
    file = open(file_name, "r")

    # figure out what the next available pages are
    # based on what's written in the current page
    options_as_strings = file.readline().replace('\n','').split('|')
    options = []
    for num in options_as_strings:
        options.append(int(num))

    # read the rest of the current page
    page_contents = file.read()

    # display the current page
    print(page_contents)

    # ask the user which page to turn to,
    # and check that they're allowed to turn to that page
    page_num = input("\nWhich page would you like to turn to next? ")
    while int(page_num) not in options:
        page_num = input("You can choose between these pages: " + str(options) + ". Please choose a valid page. ")
