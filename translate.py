from google.cloud import translate_v2 as translate
import six
import csv

target = 'en'
translate_client = translate.Client()


csv_file_male = open('arabic_names.csv','r')
csv_file_female = open('arabic_names_females.csv','r')
csv_file = open('muslim_names.csv','w')

csv_reader_male = csv.reader(csv_file_male)
csv_reader_female = csv.reader(csv_file_female)
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['num.','name', 'arabic', 'sex','meaning','meaning_en'])

count = 0

for line in csv_reader_male:
    text = line[-1]
    if(line[0] == 'Sr.'):
        continue
    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    result = translate_client.translate(text, target_language=target)
    count +=1
    # print(u"Text: {}".format(result["input"]))
    # print(u"Translation: {}".format(result["translatedText"]))
    # print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))
    print(count,end=" ")
    csv_writer.writerow([count,line[1],line[2],line[3],line[4],result["translatedText"]])
csv_file_male.close()
for line in csv_reader_female:
    text = line[-1]
    if(line[0] == 'Sr.'):
        continue
    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    result = translate_client.translate(text, target_language=target)
    count +=1
    # print(u"Text: {}".format(result["input"]))
    # print(u"Translation: {}".format(result["translatedText"]))
    # print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))
    print(count,end=" ")
    csv_writer.writerow([count,line[1],line[2],line[3],line[4],result["translatedText"]])

csv_file_female.close()
csv_file.close()
# text = 'قبل از دوپہر , وقت چاشت'
# text = 'ایک خوشبو، مائل ہونا'
# text = 'چھوٹا خوبصورت، نفیس'

