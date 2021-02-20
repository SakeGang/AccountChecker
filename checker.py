import requests, time
print("""


 _____       _          _____ _               _             
/  ___|     | |        /  __ \ |             | |            
\ `--.  __ _| | _____  | /  \/ |__   ___  ___| | _____ _ __ 
 `--. \/ _` | |/ / _ \ | |   | '_ \ / _ \/ __| |/ / _ \ '__|
/\__/ / (_| |   <  __/ | \__/\ | | |  __/ (__|   <  __/ |   
\____/ \__,_|_|\_\___|  \____/_| |_|\___|\___|_|\_\___|_|   
                                                            
                                                            
""")
print("""
[1] Minecraft Checker
[2] Spotify Checker
[3] Gmail Checker
[4] Uplay Checker
[5] Steam Checker 
[6] Origin Checker
""")
while True:
	choice = input("Choice: ")
	
	if choice == "1":
		print("Minecraft checker")

	if choice == "2":
		print("spotify checker")

	if choice == "3":
		print("gmail checker")

	if choice == "4":
		print("uplay checker")

	if choice == "5":
		print("steam checker")

	if choice == "6":
		print("origin checker")
