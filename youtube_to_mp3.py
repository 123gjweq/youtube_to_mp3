import requests
import time

print("***This script downloads music from youtube using the mp3-convert API and saves it as an mp3 file***")
id_ov_vid = input("Enter your youtube video ID (https://www.youtube.com/watch?v={ENTER THIS PART}): ")

counter = 0
headers = {
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "en-US,en;q=0.9",
	"Connection": "keep-alive",
	"Referer": "https://mp3-convert.org/",
	"sec-ch-ua-mobile": "?0",
	"Sec-Fetch-Dest": "document",
	"Sec-Fetch-Mode": "navigate",
	"Sec-Fetch-Site": "cross-site",
	"Upgrade-Insecure-Requests": "1",
}

print("Fetching download URL...")

while counter < 10:
	params = {
		"r": "hudar1255",
		"id": id_ov_vid,
		"t": round(time.time()),
		}
	try:
		r = requests.get(f"https://mp3-convert.org/get.php?", params = params, headers = headers)
		download_url = r.json()["download_url"]
		title = r.json()["title"]
		download_url[2]
		break
	except:
		print("Failed to fetch download URL...")
		print("retrying...")
	counter += 1

if counter != 10:
	print("Fetched download URL!")
	print("Attempting to download...")

	with open(f"{title}.mp3", "wb") as file:
		r = requests.get(download_url, headers = headers)
		file.write(r.content)

	print("Downloading finished!")
else:
	print("Failed too many times...")
	print("Make sure you entered the ID correctly. Check the README for more info.")

input()