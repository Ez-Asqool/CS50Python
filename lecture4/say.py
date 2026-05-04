import cowsay
import sys

# if len(sys.argv) == 2:
#     cowsay.cow("Hello, " + sys.argv[1])

if len(sys.argv) == 2:
    cowsay.trex("Hello, " + sys.argv[1])


"""
    APIs: refers to third-party services that I can write code that talk to.
    * many APIs live on the internet

    - how can i talk to APIs , connect to it and dowenload some data 
        that I can then incorporate into my own program. ??

    -> python have a very popular package that i can install via pip calle #(requests)
        the requests library allows me to make web request/internet requests using python code 
"""