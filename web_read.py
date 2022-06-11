from gtts import gTTS


import urllib.request as req

from bs4 import BeautifulSoup


url =str(input("音声化したいサイトのURLを入力してください"))
res = req.urlopen(url)



html = res
soup = BeautifulSoup(html, 'html.parser')
#print("タイトル:"+ soup.title.text)
#print("本文:"+ soup.find(id="main").text)
#contents = soup.find('div', class_="single_article_contents")
#print(contents.get_text())


mytext = "タイトル:" + soup.title.text+ "本文:"+ soup.get_text()
tts = gTTS(text=mytext, lang='ja')
tts.save(soup.title.text+'.mp3')

print("webからテキストデータを取得して音声データを作成しました")

#