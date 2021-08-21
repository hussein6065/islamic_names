from requests_html import HTMLSession
import csv 

def male():
    session = HTMLSession()
    csv_file = open('arabic_names.csv','w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['num.','name', 'arabic', 'sex','meaning'])

    # for index in range(1,196):
    #     page = f'https://www.urdupoint.com/names/boys-islamic-names-urdu/{index}.html'
        
    #     r = session.get(page)
    #     row = r.html.find('tr',first=True)
    #     print(row.text)
    for index in range(1,196):
        page = f'https://www.urdupoint.com/names/boys-islamic-names-urdu/{index}.html'
            
        r = session.get(page)
        rows = r.html.find('tr')
        
        for i in rows:
            data = i.text.split('\n')
            if(data[0] == 'Sr.'):
                continue
            try:
                csv_writer.writerow([int(data[0]),data[1],data[2],'m',data[3]])
            except Exception as e:
                continue
                
    csv_file.close()

def female():
    session = HTMLSession()
    print('Started')
    csv_file = open('arabic_names_females.csv','w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['num.','name', 'arabic', 'sex','meaning'])

    # for index in range(1,196):
    #     page = f'https://www.urdupoint.com/names/boys-islamic-names-urdu/{index}.html'
        
    #     r = session.get(page)
    #     row = r.html.find('tr',first=True)
    #     print(row.text)

   
    for index in range(1,173):
        page = f'https://www.urdupoint.com/names/girls-islamic-names-urdu/{index}.html'
            
        r = session.get(page)
        rows = r.html.find('tr')
        
        for i in rows:
            data = i.text.split('\n')
            if(data[0] == 'Sr.'):
                continue
            try:
                csv_writer.writerow([int(data[0]),data[1],data[2],'f',data[3]])
            except Exception as e:
                continue
                
    csv_file.close()
    print('Ended')


if(__name__ == '__main__'):
    female()

    'تدوین'