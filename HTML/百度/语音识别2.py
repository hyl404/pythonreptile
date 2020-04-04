from aip import AipSpeech
APP_ID = '19231821'
API_KEY = 'fMbeWhqXH6BZXMIZoBNTU5Hg'
SECRET_KEY = 'zXOOvoXC81odMKUwwTpLwHp9tYXXYd4V'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
txt="我说一个事实，这是一个新冠肺炎ICU患者的医疗费用"
# zh 中文 ； 1 windows
result = client.synthesis(txt, 'zh', 1, {
    "vol": 10,  # 音量
    "spd": 3,  # 语速
    "pit": 3,  # 语调
    "per": 1,  # 音色
})
with open("audio.mp3", "wb") as f:
    f.write(result)