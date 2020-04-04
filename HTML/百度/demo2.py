from aip import AipOcr
APP_ID = '19231161'
API_KEY = '0u2VhMCyIoZcchRnNTELhdZI'
SECRET_KEY = 'EsiR966mXAlIua89WzyQZB2gcu6Q5gTr '
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
filepath =r'E:\test\venv\百度'+'\\'+'example.jpg'
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
image = get_file_content('example.jpg')
response = client.basicGeneral(image);
#print(response['words_result'])
all_text=''
for i in response['words_result']:
    all_text += i['words']+'\n'
print(all_text)