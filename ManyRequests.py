import requests


def downloader():

    baseurl = 'https://stepic.org/media/attachments/course67/3.6.3/'

    with open('input.txt', 'r') as fin:
        urlwithname = fin.readline().strip()

    file = requests.get((urlwithname).strip())
    filename = file.text
    while True:
        url = baseurl + filename
        nextfile = requests.get(url.strip())
        print(nextfile.text)
        if nextfile.text.splitlines()[0][0] == 'We':
            print('***')
            print(nextfile.text)
            print('***')
            break
        else:
            filename = nextfile.text.splitlines()[0]


if __name__ == "__main__":
    downloader()

