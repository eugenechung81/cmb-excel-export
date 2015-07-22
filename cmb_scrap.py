from time import sleep
import urllib
import csv
from selenium import webdriver

driver = webdriver.Firefox()

def go(path):
    return driver.get(path)

def find(path):
    return driver.find_element_by_xpath(path)

def finds(path):
    return driver.find_elements_by_xpath(path)

def get_all_links():
    links = []
    profiles = finds('//*[@id="content-wrapper"]/div/div/a')
    for p in profiles:
        links.append(p.get_attribute('href'))
    return links

def download_profiles_pics(link):
    id = link[44:]
    go(link)
    image = find('//*[@id="main-photo"]').get_attribute('src')
    image_file = 'images/' + id + '-1.jpg'
    urllib.urlretrieve(image, image_file)
    print 'Downloading [' + image_file + ']'
    num_of_images = len(driver.find_elements_by_xpath('//*[@id="arrow"]/div/div'))
    for n in xrange(2,num_of_images+1):
        find('//*[@id="next"]').click()
        image = find('//*[@id="main-photo"]').get_attribute('src')
        image_file = 'images/' + id + '-' + str(n) + '.jpg'
        urllib.urlretrieve(image, image_file)
        print 'Downloading [' + image_file + ']'

def get_csv_row(link, headers):
    # link = 'https://coffeemeetsbagel.com/bagels/matched/5659010'
    go(link)
    details = finds('//*[@id="main"]/div[2]/div[2]/p')
    bagel_row = {}
    for d in details:
        line = str(d.text.encode('utf8'))
        try:
            if line.startswith('Education'):
                bagel_row['Education'] = line.split('\n')[1:]
            elif line.startswith('I am'):
                bagel_row['Description'] = line
            else:
                key,value = str(d.text).split('\n')
                bagel_row[key]=value
        except:
            print 'ERROR : ' + line.replace('\n',': ')
            pass

    id = link[44:]
    bagel_row['Id'] = id
    bagel_row['Url'] = link
    bagel_row['Image-1'] = 'C:\\Dropbox\\projects-python\\automated-testing\\images\\' + id + '-1.jpg'
    num_of_images = len(driver.find_elements_by_xpath('//*[@id="arrow"]/div/div'))
    for n in xrange(2,num_of_images+1):
        find('//*[@id="next"]').click()
        bagel_row['Image-' + str(n)] = 'C:\\Dropbox\\projects-python\\automated-testing\\images\\' + id + '-' + str(n) + '.jpg'

    row = [bagel_row[h] if h in bagel_row.keys() else '' for h in headers]

    print 'Downloaded: %s' % (row)

    return row

# Start
headers = ['Id', 'Name', 'Age', 'Height', 'Current City', 'Description', 'Employer', 'Religion', 'Home Country', 'Nationality', 'Education', 'Ethnicity', 'Occupation', 'Url', 'Image-1', 'Image-2', 'Image-3', 'Image-4']
# headers = ['Id', 'Name', 'Age', 'Height', 'Occupation', 'Url', 'Image-1', 'Image-2', 'Image-3', 'Image-4']
go("https://coffeemeetsbagel.com/bagels/history/")
links = get_all_links()

go("https://coffeemeetsbagel.com/bagels/history/?page=4")
links.extend(get_all_links())
len(links)
print links

# https://coffeemeetsbagel.com/bagels/history/?page=2
# https://coffeemeetsbagel.com/bagels/history/?page=3
# https://coffeemeetsbagel.com/bagels/history/?page=4

# https://coffeemeetsbagel.com/bagels/matched/6049617
# https://coffeemeetsbagel.com/bagels/matched/6092846

rows = []
for link in links:
# for link in links[:10]:
    try:
        download_profiles_pics(link)
        sleep(1)
        row = get_csv_row(link, headers)
        rows.append(row)
        print 'Processed: ' + str(len(rows))
        sleep(1)
    except:
        print 'Error in ' + link


# OUTPUT

f = open("bagels-all.csv", 'w')
writer = csv.writer(f)
writer.writerow(headers)
for r in rows:
    writer.writerow(r)
f.close()



# Test Individual
get_csv_row('https://coffeemeetsbagel.com/bagels/matched/5788628',headers)
get_csv_row('https://coffeemeetsbagel.com/bagels/matched/5659010',headers)

