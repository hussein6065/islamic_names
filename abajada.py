from requests_html import HTMLSession
import csv 
def abajada():
    session = HTMLSession()
    # csv_file = open('abajada.csv','w')
    # csv_writer = csv.writer(csv_file)
    # csv_writer.writerow(['letter.','value'])

    page = 'https://en.wikipedia.org/wiki/Abjad_numerals'
        
    r = session.get(page)
    rows = r.html.find('table')
    

    count = 0
    print(rows[10].html.find('tr'))
    # print(rows[11].text)
    # print(rows[12].text)
    # for i in rows:
    #     count += 1
    #     # data = i.text.split('\n')
    #     print(i.html)
    #     print(f"-------------------------------{count}-------------------------")
    #     # if(data[0] == 'Sr.'):
    #     #     continue
        # try:
        #     csv_writer.writerow([int(data[0]),data[1],data[2],'m',data[3]])
        # except Exception as e:
        #     continue
                
    # csv_file.close()




if(__name__ == '__main__'):
    abajada()