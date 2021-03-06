import requests
from bs4 import BeautifulSoup

urls = ['https://www.sanfoundry.com/data-structure-questions-answers-linear-search-iterative/']

i = 1216
text = ''

for url in urls:
    print('Getting:\n', url)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    div = soup.find('div', 'inside-article')

    # Getting next Link
    for anchor in div.find_all('a', href=True):
        if str(anchor).__contains__('Next'):
            urls.append(str(anchor['href']))
            break

    for line in div.text.splitlines():
        if line != '' and line != 'advertisement':
            if not line.__contains__('Next') and not line.__contains__('Prev'):
                if line.__contains__('Post navigation'):
                    break

                if not line.__contains__('Sanfoundry') and not line.__contains__(
                        '1000+ Multiple Choice Questions') and not line.__contains__(
                    'Instagram') and not line.__contains__('Data Structure'):
                    if line[0].isnumeric():
                        if line.__contains__('.'):
                            text += '\n'
                            question = line[line.index('.') + 1:]
                            text += str(i) + '.' + question + '\n'
                            i += 1
                        else:
                            text += line + '\n'
                    else:
                        text += line + '\n'

file = open('mcqs-ds.txt', 'a')
file.write(text)
file.close()

print('Done')
