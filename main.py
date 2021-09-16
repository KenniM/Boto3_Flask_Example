from flask import Flask, request, jsonify
import csv
import boto3
import base64

with open('Rekognition_Credentials.csv','r') as input:
    next(input)
    reader=csv.reader(input)
    for line in reader:
        accesss_key_id=line[2]
        secret_access_key=line[3]

client=boto3.client('rekognition',
aws_access_key_id=accesss_key_id, aws_secret_access_key=secret_access_key,
region_name='us-east-2')

app = Flask(__name__)

@app.route("/tarea3-201800457")
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

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)