import speech_recognition as sr
from gtts import gTTS
import os



def command():
	with sr.Microphone() as source:
		print("Say Something ")
		r=sr.Recognizer()
		r.energy_threshold=500
		audio=r.listen(source)
	try:
		print('\n'+r.recognize_google(audio))
	except:
		pass
	word=r.recognize_google(audio)
	return word

def assistant(word):
	if "who created you" in word :
		text_to_speech = gTTS(text='I was Created by The Sam Techtrons', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')

	if "give your introduction" in word:
		text_to_speech = gTTS(text='I am Your Health Assistant', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')

	if "what can you do" in word:
		text_to_speech = gTTS(text='I can give you some tips for your health and i can also prescribe Medicines for You', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')

	if "I am suffering from fever" in word:
		text_to_speech = gTTS(text='You can take paracetamol or asprin..Thank you', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from headache" in word:
		text_to_speech = gTTS(text='You can take disprin..Thank you', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from cough and cold" in word:
		text_to_speech = gTTS(text='You can take amoxicillin..Thank you', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from diabetes" in word:
		text_to_speech = gTTS(text='You can take insulin lispro ..Thank you', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from stomach ache" in word:
		text_to_speech = gTTS(text='You can take panadol..Thank you', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from skin allergies" in word:
		text_to_speech = gTTS(text='You can take allegra..Thank you', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from vomiting" in word:
		text_to_speech = gTTS(text='You can take dolasetron..Thank you', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from depression" in word:
		text_to_speech = gTTS(text='You can take lexapro..Thank you', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from chicken pox" in word:
		text_to_speech = gTTS(text='You can take a cool bath with added baking soda and you can also take benadryl', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from arthritis" in word:
		text_to_speech = gTTS(text='You can take immunosupressive drug and analgesic', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from asthma" in word:
		text_to_speech = gTTS(text='You have to quit smoking and can take anti inflammatory drug', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from bipolar disorder" in word:
		text_to_speech = gTTS(text='You can take antipsychotic drugs ', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from chest pain" in word:
		text_to_speech = gTTS(text='You can take nitroglycerine drugs', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from conjunctvitis" in word:
		text_to_speech = gTTS(text='You can maintain hygeine and self heal with cold compress', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from constipation" in word:
		text_to_speech = gTTS(text='You can take stool softener and fibre supplement', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from dehydration" in word:
		text_to_speech = gTTS(text='You can take oral rehydration solution', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from food poison" in word:
		text_to_speech = gTTS(text='ensure adequate hydration and take rehydration solution', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from flu" in word:
		text_to_speech = gTTS(text='You can take bed rest and antiviral drug ', lang ='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from indigestion" in word:
		text_to_speech = gTTS(text='You can take antacids and oral suspension medicines', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from insomnia" in word:
		text_to_speech = gTTS(text='You can take sedatives and anti depressants', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from malaria" in word:
		text_to_speech = gTTS(text='You can take anti parasites and antibiotics ', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from malnutrition" in word:
		text_to_speech = gTTS(text='You can high protein diet and nutiritive suppliments', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from obesity" in word:
		text_to_speech = gTTS(text='You  have to do physical exercise and take low fat diet', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from panic disorder" in word:
		text_to_speech = gTTS(text='You can take anti depressants', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from scabies" in word:
		text_to_speech = gTTS(text='You can take anti parasite drugs', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from yellow fever" in word:
		text_to_speech = gTTS(text='You can take oral rehydration therapy and in critical case consult doctor', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')
	if "I am suffering from acne" in word:
		text_to_speech = gTTS(text='You can apply aloe vera and take vitamin a derivatives', lang='en')
		text_to_speech.save('audio.mp3')
		os.system('mpg123 audio.mp3')


 

	
while True:
    assistant(command())