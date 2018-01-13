from datetime import datetime


def handler(event, context):
    print("Invoked at ", datetime.now())
    return "You got me"
