from flask import Flask, request, jsonify
import csv
import boto3
import base64

# Reading a CSV that contains the AWS Credentials

with open('Rekognition_Credentials.csv','r') as input:
    next(input)
    reader=csv.reader(input)
    for line in reader:
        accesss_key_id=line[2]
        secret_access_key=line[3]

# Creating a Rekognition client

client=boto3.client('rekognition',
aws_access_key_id=accesss_key_id, aws_secret_access_key=secret_access_key,
region_name='us-east-2')

# Creating a Flask app

app = Flask(__name__)

# Add a route

@app.route("/my-route")
def showData():
    content = request.json
    image = content['base64']
    imageBuffer=base64.b64decode(image)

    response = client.detect_labels(
        Image={
            'Bytes':imageBuffer
        },
        MaxLabels=123
    )

    return jsonify({"Result":response})

# Start the app on localhost, the port will be given by Flask

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)
