import requests

DIR_NAME = 'data'
URL_TEMPLATE = 'https://raw.githubusercontent.com/wesm/pydata-book/2nd-edition/datasets/babynames/yob{0}.txt'
files_counter = 0
for year in range(1880, 2011):
    url = URL_TEMPLATE.format( str(year) )
    response = requests.get(url)
    if response.ok:
        file_path = DIR_NAME + '/' + str(year) + '.txt'
        with open(file_path, 'w') as f:
            f.write(response.content.replace('\r\n', '\n'))
        files_counter += 1
        print('{0} saved'.format(file_path))
print('{0} files loaded.'.format( str(files_counter) ))