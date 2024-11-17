import json

def lambda_handler(event, context):
    # failsafe for no event
    if not event:
        return {
            'statusCode': 400,
            'body': json.dumps('No event received.')
        }
    
    # failsafe for no httpMethod kinda overkill since api gateway does not allow other methods
    if event["httpMethod"] == "POST":
        
        # failsafe for no body
        if event["body"] != None:
            body = json.loads(event["body"])
            # check for the key "name"
            if "text" in body:
                return {
                    'statusCode': 200,
                    'body': json.dumps(body["text"].upper())
                }
            return {
                'statusCode': 400,
                'body': json.dumps(f"""No key "text" in body: {body}""")
            }    
            
        return {
            'statusCode': 400,
            'body': json.dumps(f'Body is empty.')
        }
    
    return {
        'statusCode': 405,
        'body': json.dumps(f'Method not allowed: {event["httpMethod"]}')
    }