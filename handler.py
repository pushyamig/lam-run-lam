import boto3
import os

lam = boto3.client('lambda')

def hello(event, context):
    print("You are in the hello() function")
    try:
        invoking_func_name = os.environ['invoke_func_name']
        time_to_invoke_lambda = os.environ['count']
        print(invoking_func_name + " : "+time_to_invoke_lambda)
        for i in range(int(time_to_invoke_lambda)):
            response = lam.invoke(FunctionName=invoking_func_name,
                                  InvocationType='RequestResponse')
            print('Run {} What is in the response {} '.format(i,response))

    except Exception as e:
        print(e)
        raise e
