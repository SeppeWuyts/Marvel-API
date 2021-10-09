#import modules
import urllib.parse
import hashlib
import requests
#main api link and timestamp, which is needed for accessing the marvel api
main_api = "https://gateway.marvel.com:443/v1/public/characters?"
timestamp = "1"
while True:
    #ask the user for their public and private key, if they type "q", the program terminates
    public_key = input("Type your public key (type 'q' to quit):")
    if public_key == "quit" or public_key == "q":
        break
    private_key = input("Type your private key (type 'q' to quit):")
    if private_key == "quit" or public_key == "q":
        break
    #hashing the timestamp and keys, the marvel api requires a hash of these to be sent along with the request
    hash_code = timestamp + private_key + public_key
    hash_result = hashlib.md5(hash_code.encode())
    #ask for char name
    char_name = input("Type the name of the character you want to look up(type 'q' to quit):")
    if char_name == "quit" or char_name == "q":
        break
    #constructing the url for the request and printing it to verify
    url = main_api + urllib.parse.urlencode({"name": char_name, "ts": timestamp, "apikey": public_key, "hash": hash_result.hexdigest()})
    print("URL: " + (url))
    #get the json data from the request and check the status
    json_data = requests.get(url).json()
    json_status = json_data["code"]
    print(json_status)
    if json_status == 200:
        #print a success message
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        #get the character name and description from teh json data and print it
        print("Character: " + str(json_data["data"]["results"][0]["name"]))
        print("Character: " + (json_data["data"]["results"][0]["description"]))
        print("=============================================\n")
    #if the status is not okay, show one of these error messages
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user input")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Status Code: " + str(json_status) + "; Refer to:")
        print("https://developer.marvel.com/documentation/authorization")
        print("************************************************************************\n")
