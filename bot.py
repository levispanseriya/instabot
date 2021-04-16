from instabot import Bot
import glob,os

bot = Bot()

bot.login(username = "username", password = "password" )

os.chdir("img")

for file in glob.glob("*.jpg"):
    bot.upload_photo(file,caption = "123456")
