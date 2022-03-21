from requests import get

from re import findall

import os

import glob

from rubika.client import Bot

import requests

from rubika.tools import Tools

from rubika.encryption import encryption

from gtts import gTTS

from mutagen.mp3 import MP3

import time

import random

import urllib

import io

bot = Bot("AUTH")

target = "GUID"

answered = [bot.getGroupAdmins]

retries = {}

sleeped = False

# delmess = ["دولی","کصکش","کون","کص","کیر" ,"خر","کستی","دول","گو","کس","کسکش","کوبص"]

plus= True

while True:

	try:		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]

		min_id = bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]

		while True:

			try:

				messages = bot.getMessages(target,min_id)

				break

			except:

				continue

		

		open("id.db","w").write(str(messages[-1].get("message_id")))

		for msg in messages:

			if msg["type"]=="Text" and not msg.get("message_id") in answered:

				if not sleeped:

					if msg.get("text") == "روشن" and msg.get("author_object_guid") in admins :

						bot.sendMessage(target, "ربات اکنون فعال است ✅", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("افزودن") :

						bot.invite(target, [bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"]])

						bot.sendMessage(target, "کاربر به گپ اضافه شد ✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "دستورات":

						bot.sendMessage(target, "دستورات بات\n سلام\nبات\nربات\nگوربه\nرل زدم\nدخترم\nزندگی من کیهه\nامیررر\nسید\nگودرت\nحاجی\nربات کیه\nاصل میدی؟\nممه میقام\nچخبر\nجنده\nممه\nخوبید\nجنده\nکصکش\nبوس بده\nداستان\nدرد\nدیوث\nدرد\nبلک استار\nخوبی عزیزم\nخوبی\nجوک\nچتوری\nعشقم\nخبی\n دانلود سطح \nیچیزی بگو\nسکوت 9999\n😐🗿😐😐🗿😐😂🗿😂😂🗿😂😐🗿\nجوک=جوک میگه براتون😁\nفونت =فونت اسمتون رو میفرسته پیویتون به طور مثال فونت black star\nتاریخ=تاریخ رو میگه بتون\nساعت=ساعت رو به طور دقیق\nتست=فعال بودن بات رو نشون میده\nخاموش=بات خاموش میشه\nروشن=بات روشن میشه\nبپاک=ریپلای روی پیام مورد نظر و گفتن بپاک ربات خودکار پاک میکنه\nقفل =با گفتن این کلمه قفل خودکار گپ فعال میشه و گپ قفل میشه\nباز =با گفتن این کلمه گپ باز میشه\nبن=روی کاربر مورد نظر ریپلای کرده و کلمه بن را بگویید \nلینک =درخواست لینک میکنید و به شما لینک می‌دهد!")

					elif msg.get("text").startswith("!cal"):

						msd = msg.get("text")

						if plus == True:

							try:

								call = [msd.split(" ")[1], msd.split(" ")[2], msd.split(" ")[3]]

								if call[1] == "+":

									am = float(call[0]) + float(call[2])

									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))

									plus = False

							

								elif call[1] == "-":

									am = float(call[0]) - float(call[2])

									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))

							

								elif call[1] == "*":

									am = float(call[0]) * float(call[2])

									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))

							

								elif call[1] == "/":

									am = float(call[0]) / float(call[2])

									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))

							except IndexError:

								bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌" ,message_id=msg.get("message_id"))

						plus= True

					elif msg.get("text").startswith("!send") :

						bot.sendMessage(bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"], "شما یک پیام ناشناس دارید:\n"+" ".join(msg.get("text").split(" ")[2:]))

						bot.sendMessage(target, "پیام ارسال شد ✅", message_id=msg.get("message_id"))

   

					elif msg.get("text") == "سلام":

						bot.sendMessage(target, "علیک", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "گودرت":

						bot.sendMessage(target, "اره داش من گدرتمندم", message_id=msg.get("message_id"))

					

					elif msg.get("text") == "دانلود سطح":

						bot.sendMessage(target, "فرایند دانلود سطح برای این نوب آغاز شد.⇧⇧⇧████████▓▓▓70درصد❌ارور 404 این فرد یک نوب خالص است.!!!!❌", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "حاجی":

						bot.sendMessage(target, "جانم حا‌جی قربونت", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "بگو":

						bot.sendMessage(target, " سام بادی گیو می هایااااااااااااااااااااااااااااااااااااااااااااااااااااااااااااااااااااااااااااااااااااااااااااهههههههههههههههههههههه😐", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "بلک استار":

						bot.sendMessage(target, "سازندمه چیکارش داری اینم ایدیش @TOCREATE", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "سکوت 9999":

						bot.sendMessage(target, " › کاربر ›› به مدت [  6 روز و 22 ساعت و 39 دقیقه  ] سکوت شد !", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "عزیزم":

						bot.sendMessage(target, "😐جون", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "رل":

						bot.sendMessage(target, "منم رل میخام", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "اطلاعیه":

						bot.sendMessage(target, "پس از مرگ کیان !!! مختار مجبور به متحد شدن با جومونگ شد 🙂💔", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "😐":

						bot.sendMessage(target, "چه مرگته", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "😐😐":

						bot.sendMessage(target, "دردت چیست", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "سید":

						bot.sendMessage(target, "جان سید ،سید فدات شه😃", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "گشنمه":

					    bot.sendMessage(target, "بیا اینو بخور😐", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "کس":

						bot.sendMessage(target, "بی ادب", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "هک":

						bot.sendMessage(target, "😂قدیمی شده", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "بوس":

						bot.sendMessage(target, "💋لب میدم", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "چایی":

						bot.sendMessage(target, "بفرما چایی😝☕️", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "اومدم":

						bot.sendMessage(target, "خوش اومدی", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "بیشعور":

						bot.sendMessage(target, "در حال پاکسازی بی شعور❌\nدر حال نصب شعور...\nn██████████▓99درصد\nارور407🥀💔\nاین فرد ذاتی بیشعور است و قابلیت نصب شعور برای آن وجود ندارد.!", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "احمق":

						bot.sendMessage(target, "احمق هفت جدته😐💔", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "ربات کیه":

						bot.sendMessage(target, "بلک استار", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "اصل" and msg.get("author_object_guid") in admins :

						bot.sendMessage(target, "ربات هستم 1 ساعت از بلک استار", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "مهدی" and msg.get("author_object_guid") in admins :

						bot.sendMessage(target, "جان", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "چخبر":

						bot.sendMessage(target, "دسته تبر", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "جنده":

						bot.sendMessage(target, "عمته", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "لینک گپ" and msg.get("author_object_guid") in admins :

						bot.sendMessage(target, "https://rubika.ir/joing/CAIDCHEG0CYXRPWGIOUALQBOKQFPYXAX", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "صگ" and msg.get("author_object_guid") in admins :

						bot.sendMessage(target, "یعنی روبیکا صگ داره ", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "ربات":

						bot.sendMessage(target, "مزاحم نشو شماره نمیدم", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "مست":

						bot.sendMessage(target, "با اب میوه مست کردی", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "بات":

						bot.sendMessage(target, "مزاحم نشو", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "لینک":

						bot.sendMessage(target, "https://rubika.ir/joinc/BECEFCJD0SUPQTJIGRECQCANTLWHNNMR", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "ممه":

						bot.sendMessage(target, "ندارم", message_id=msg.get("message_id"))

			

					elif msg.get("text") == "درد":

						bot.sendMessage(target, "تو جونت 😘💋", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "خوبی عزیزم":

						bot.sendMessage(target, "مرسی تو خوبی قشنگم؟ اصل میدی؟🤓🫂", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "خبی":

						bot.sendMessage(target, "تو فکر کن بدم", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "خوبید":

						bot.sendMessage(target, "نه من خوب نیستم", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "افرین":

						bot.sendMessage(target, "هزار افرین‌بهت", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "چتوری":

						bot.sendMessage(target, "مثل پلو تو دوری 😐چقدر زر میزنی بچه", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "قوانین":

						bot.sendMessage(target, "لینک ممنوع😐\nفوش ممنوع\nدعوا ممنوع\nمخ زنی آزاده\nبقیه چیزام ازاده راحت باش🙂😂", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "جق":

						bot.sendMessage(target, "در جوانی تا توانی منت کص‌ را نکش دستت را حلقه کن بر قامت کیرت بکش", message_id=msg.get("message_id"))

					

					elif msg.get("text") == "ممه میقام":

						bot.sendMessage(target, "بیا میمه ۸۵ بقول🙂🍼", message_id=msg.get("message_id"))

					

					elif msg.get("text") == "خوبی":

						bot.sendMessage(target, "خوب نیستم ۱۰۰۰ تومن شارژ بده تا خوب شم", message_id=msg.get("message_id"))

					

					elif msg.get("text") == "نوب":

						bot.sendMessage(target, "یک عدد نوب یافت شد❌\nدرحال پاکسازی ویروس نوب بودن😐\n█▓▓▓▓▓▓▓▓▓10درصد \n██▓▓▓▓▓▓▓▓20درصد\n███▓▓▓▓▓▓▓30درصد\n████▓▓▓▓▓▓40درصد\n█████▓▓▓▓▓50درصد\n██████▓▓▓▓60درصد\n███████▓▓▓70درصد\n████████▓▓80درصد\n█████████▓90درصد\n██████████ 100 درصد✅\nپاکسازی رو به اتمام است...✅لطفا صبور باشید🗿\nویروس نوب از روی زمین با موفقیت پاک شد.!✅🗿\n", message_id=msg.get("message_id"))

					

					elif msg.get("text") == "😂😐":

						bot.sendMessage(target, "اوففففف تو فقط بخند🤤🙃", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "کصکش":

						bot.sendMessage(target, "بشین سرش کیسه بکش", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "😂😂":

						bot.sendMessage(target, "نخند زشت میشی", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "😐😂":

						bot.sendMessage(target, "جوننننن تو فقط بخند🤤💋", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "عشقم":

						bot.sendMessage(target, "عشقت لب میخاست بش ندادی عبضی🥲", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "جون":

						bot.sendMessage(target, "لب میدی یا کــو‌‌نـ", message_id=msg.get("message_id"))

					

					elif msg.get("text") == "نوب":

						bot.sendMessage(target, "یک عدد نوب یافت شد❌\nدرحال پاکسازی ویروس نوب بودن😐\n█▓▓▓▓▓▓▓▓▓10درصد \n██▓▓▓▓▓▓▓▓20درصد\n███▓▓▓▓▓▓▓30درصد\n████▓▓▓▓▓▓40درصد\n█████▓▓▓▓▓50درصد\n██████▓▓▓▓60درصد\n███████▓▓▓70درصد\n████████▓▓80درصد\n█████████▓90درصد\n██████████ 100 درصد✅\nپاکسازی رو به اتمام است...✅لطفا صبور باشید🗿\nویروس نوب از روی زمین با موفقیت پاک شد.!✅🗿\n", message_id=msg.get("message_id"))

					

					elif msg.get("text") == "مدی":

						bot.sendMessage(target, "رل میخاد", message_id=msg.get("message_id"))

						

					elif msg.get("text") == "دیوث":

						bot.sendMessage(target, "کم گوه بخور خودتی🙂💔", message_id=msg.get("message_id"))

					if  msg.get("text").startswith('!user @'):

						try:

							user_info = bot.getInfoByUsername( msg.get("text")[7:])

							if user_info['data']['exist'] == True:

								if user_info['data']['type'] == 'User':

									bot.sendMessage(target, 'Name User:\n ' + user_info['data']['user']['first_name'] + ' ' + user_info['data']['user']['last_name'] + '\n\nBio User:\n ' + user_info['data']['user']['bio'] + '\n\nGuid:\n ' + user_info['data']['user']['user_guid'] ,  msg.get('message_id'))

									print('sended response')

								else:

									bot.sendMessage(target, 'کانال است ❌' ,  msg.get('message_id'))

									print('sended response')

							else:

								bot.sendMessage(target, "کاربری وجود ندارد ❌" ,  msg.get('message_id'))

								print('sended response')

						except:

							print('server bug6')

							bot.sendMessage(target, "خطا در اجرای دستور مجددا سعی کنید ❌" ,message_id=msg.get("message_id"))

							

					elif msg.get("text") == "خاموش" and msg.get("author_object_guid") in admins :

						sleeped = True

						bot.sendMessage(target, "ربات خاموش شد ✅", message_id=msg.get("message_id"))

			

					elif msg.get("text").startswith("بیو"):

						

							try:

								response = get("https://api.codebazan.ir/bio/").text

								bot.sendMessage(target, response,message_id=msg.get("message_id"))

							except:

								bot.sendMessage(target, "ببخشید، خطایی پیش اومد!", message_id=msg["message_id"])		

						

					elif msg.get("text").startswith("داستان") or msg.get("text").startswith("!dastan"):

						

						try:

							response = get("http://api.codebazan.ir/dastan/").text

							bot.sendMessage(target, response,message_id=msg.get("message_id"))

						except:

							bot.sendMessage(target, "مشکلی پیش اومد!", message_id=msg["message_id"])

						

					elif msg.get("text").startswith("دانستنی"):

						

						try:

							response = get("http://api.codebazan.ir/danestani/").text

							bot.sendMessage(target, response,message_id=msg.get("message_id"))

						except:

							bot.sendMessage(target, "دستورت رو اشتباه وارد کردی", message_id=msg["message_id"])

							

					elif msg.get("text").startswith("همسر"):

							try:

								response = get("https://api.codebazan.ir/name/?type=json").text

								bot.sendMessage(target, response,message_id=msg.get("message_id"))

							except:

								bot.sendMessage(target, "دستورت رو اشتباه وارد کردی", message_id=msg["message_id"])		

			

					elif msg.get("text").startswith("پ ن پ") or msg.get("text").startswith("!pa-na-pa") or msg.get("text").startswith("په نه په"):

						

						try:

							response = get("http://api.codebazan.ir/jok/pa-na-pa/").text

							bot.sendMessage(target, response,message_id=msg.get("message_id"))

						except:

							bot.sendMessage(target, "شرمنده نتونستم بفرستم!", message_id=msg["message_id"])

							

					elif msg.get("text").startswith("بورس"):

							

						try:

							response = get("https://api.codebazan.ir/bours/").text

							bot.sendMessage(target, response,message_id=msg.get("message_id"))

						except:

							bot.sendMessage(target, "مشکلی پیش اومد!", message_id=msg["message_id"])

					

					elif msg.get("text").startswith("دیالوگ"):

						

						try:

							response = get("http://api.codebazan.ir/dialog/").text

							bot.sendMessage(target, response,message_id=msg.get("message_id"))

						except:

							bot.sendMessage(target, "متاسفانه تو ارسال مشکلی پیش اومد!", message_id=msg["message_id"])

								

					elif msg.get("text").startswith("ذکر") or msg.get("text").startswith("zekr") or msg.get("text").startswith("!zekr"):

							try:

								response = get("http://api.codebazan.ir/zekr/").text

								bot.sendMessage(target, response,message_id=msg.get("message_id"))

							except:

								bot.sendMessage(target, "ببخشید، خطایی پیش اومد!", message_id=msg["message_id"])

								

					elif msg.get("text").startswith("اخبار"):

							try:

								response = get("https://api.codebazan.ir/khabar/?kind=iran").text

								bot.sendMessage(target, response,message_id=msg.get("message_id"))

							except:

								bot.sendMessage(target, "ببخشید، خطایی پیش اومد!", message_id=msg["message_id"])		

								

					elif msg.get("text").startswith("حدیث") or msg.get("text").startswith("hadis") or msg.get("text").startswith("!hadis"):

							try:

								response = get("http://api.codebazan.ir/hadis/").text

								bot.sendMessage(target, response,message_id=msg.get("message_id"))

							except:

								bot.sendMessage(target, "ببخشید، خطایی تو ارسال پیش اومد!", message_id=msg["message_id"])

								

					elif msg.get("text").startswith("غزل"):

						

						try:

							response = get("https://api.codebazan.ir/ghazalsaadi/").text

							bot.sendMessage(target, response,message_id=msg.get("message_id"))

						except:

							bot.sendMessage(target, "مشکلی پیش اومد!", message_id=msg["message_id"])

								

					elif msg.get("text").startswith("الکی مثلا"):

						

						try:

							responser = get(f"http://api.codebazan.ir/jok/alaki-masalan/").text

							bot.sendMessage(target, responser,message_id=msg["message_id"])

						except:

							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])

					elif msg.get("text").startswith("ترجمه"):

						

						try:

							responser = get(f"https://api.codebazan.ir/translate/?type=json&from=en&to=fa&text={msg.get('text').split()[1:]}").json()

							al = [responser["result"]]

							bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text

							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])

						except:

							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])

					elif msg.get("text").startswith("فونت"):

						#print("\n".join(list(response["result"].values())))

						try:

							response = get(f"https://api.codebazan.ir/font/?text={msg.get('text').split()[1]}").json()

							bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:110])).text

							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])

						except:

							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])

								

					elif msg.get("text").startswith("جوک"):

						

						try:

							response = get("https://api.codebazan.ir/jok/").text

							bot.sendMessage(target, response,message_id=msg.get("message_id"))

						except:

							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])

							

					elif msg.get("text") == "ساعت":

						bot.sendMessage(target, f"Time : {time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}", message_id=msg.get("message_id"))

					elif msg.get("text") == "تاریخ":

						bot.sendMessage(target, f"Date: {time.localtime().tm_year} / {time.localtime().tm_mon} / {time.localtime().tm_mday}", message_id=msg.get("message_id"))

					elif msg.get("text") == "پاک" and msg.get("author_object_guid") in admins :

						bot.deleteMessages(target, [msg.get("reply_to_message_id")])

						bot.sendMessage(target, "پیام پاک شد ✅", message_id=msg.get("message_id"))

                  

					elif msg.get("text") == "گزارش" and msg.get("author_object_guid") in admins :

						bot.deleteMessages(target, [msg.get("reply_to_message_id")])

						bot.sendMessage(target, "عجب",message_id=msg.get("message_id"))

						

					elif msg.get("text") == "قفل" and msg.get("author_object_guid") in admins :

						print(bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","AddMember"]).text)

						bot.sendMessage(target, "گپ بسته شد ✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "باز" and msg.get("author_object_guid") in admins :

						bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","SendMessages","AddMember"])

						bot.sendMessage(target, "گپ باز شد ✅", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("بن") and msg.get("author_object_guid") in admins :

						try:

							guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]

							user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]

							if not guid in admins :

								bot.banGroupMember(target, guid)

								bot.sendMessage(target, f"✅ کاربر حذف شد", message_id=msg.get("message_id"))

							else :

								bot.sendMessage(target, f"❎ کاربر حذف نشد", message_id=msg.get("message_id"))

								

						except IndexError:

							a = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]

							if a in admins:

								bot.sendMessage(target, f"کاربر حذف نشد ❌", message_id=msg.get("message_id"))

							else:

								bot.banGroupMember(target, bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"])

								bot.sendMessage(target, f"کاربر حذف شد ✅", message_id=msg.get("message_id"))

				else:

					if msg.get("text") == "روشن" and msg.get("author_object_guid") in admins :

						sleeped = False

						bot.sendMessage(target, "ربات فعال شد ✅", message_id=msg.get("message_id"))

			elif msg["type"]=="Event" and not msg.get("message_id") in answered and not sleeped:

				name = bot.getGroupInfo(target)["data"]["group"]["group_title"]

				data = msg['event_data']

				if data["type"]=="RemoveGroupMembers":

					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]

					bot.sendMessage(target, f"خدانگهدار {user} 🗑️", message_id=msg["message_id"])

				

				elif data["type"]=="AddedGroupMembers":

					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]

					bot.sendMessage(target, f"سلام کاربر {user} به گروه {name} خوش اومدید 😃\nلطفا قوانین رو رعایت کن ✅ سازنده @TOCREATE", message_id=msg["message_id"])

				

				elif data["type"]=="LeaveGroup":

					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]

					bot.sendMessage(target, f"ی صگی کمتر {user} 🗑️", message_id=msg["message_id"])

					

				elif data["type"]=="JoinedGroupByLink":

					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]

					bot.sendMessage(target, f"سلام کاربر {user}  به گروه {name} خوش اومدید 😃\nلطفا قوانین رو رعایت کن ✅ سازنده @TOCREATE", message_id=msg["message_id"])

			answered.append(msg.get("message_id"))

	except KeyboardInterrupt:

		exit()

	except Exception as e:

		if type(e) in list(retries.keys()):

			if retries[type(e)] < 3:

				retries[type(e)] += 1

				continue

			else:

				retries.pop(type(e))

		else:

			retries[type(e)] = 1

			continue
