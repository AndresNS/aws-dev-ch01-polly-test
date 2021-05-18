import boto3
import json

credentials = json.load(open('credentials.json', 'r'))

polly = boto3.client('polly', region_name='us-west-2',
                     aws_access_key_id=credentials['aws_access_key_id'],
                     aws_secret_access_key=credentials['aws_secret_access_key'])

result = polly.synthesize_speech(Text='Hello world again!',
                                 OutputFormat='mp3',
                                 VoiceId='Aditi')

audio = result['AudioStream'].read()

with open('./audios/helloworld.mp3', 'wb') as file:
    file.write(audio)
