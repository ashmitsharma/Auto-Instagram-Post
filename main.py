from instagrapi import Client
import os
import shutil
import random
import logging
import json
import urllib.request
import time
import smtplib

def sendMail(message):
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("motivationalsuccesss1001@gmail.com", "rameimelxdythrve")
        s.sendmail("motivationalsuccesss1001@gmail.com", "financiary@gmail.com", message)
        s.quit()
        logging.info("Mail Sent")
    except Exception as e:
        logging.info("Not Able to send mail Sent: {}".format(e))

# this function will check internet connection and return true or false
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

# This function return the hastag set
def createCaption():
    #opening file which have hashtags and then selecting random 30 hashtags
    caption = """
Do Follow @financiary for more motivational content.
    
Like, Comment and Share with your friends.
    
    
----HashTags---- 
    """
    hashtagPath = "/home/ash/instaOperator/tmp/hashtag.txt"
    with open(hashtagPath, 'r', encoding='utf-8') as f:
        words = f.read().split()
    hashtag = ""
    for _ in range(30):
        hashtag = hashtag + " " + random.choice(words)

    return caption + hashtag

#this function will pick a random post path and return it
def getPostPath():
    postDirPath = "/home/ash/instaOperator/post/"
    selectedPostPath = random.choice(os.listdir(postDirPath))  # change dir name to whatever
    logging.info("Post Path Selected: {}".format(postDirPath + selectedPostPath))
    return postDirPath + selectedPostPath

#this function will pick a random reel path and return it
def getReelPath():
    reelDirPath = "/home/ash/instaOperator/reel/"
    selectedReelPath = random.choice(os.listdir(reelDirPath))
    logging.info("Reel Path Selected: {}".format(reelDirPath + selectedReelPath))
    dstPath = "/home/ash/instaOperator/DONE/reel/"
    os.rename((reelDirPath + selectedReelPath), (dstPath + selectedReelPath))
    return dstPath + selectedReelPath

#This function will move the uploaded post to DONE folder
def movePost(srcPath):
    dstPath = "/home/ash/instaOperator/DONE/post/"
    shutil.move(srcPath, dstPath)
    logging.info("Post Moved from {} to {}".format(srcPath, dstPath))

def changeJSON(type):
    jsonPath = "/home/ash/instaOperator/tmp/uploadData.json"
    jsonFile = open(jsonPath, "r")  # Open the JSON file for reading
    uploadData = json.load(jsonFile)  # Read the JSON into the buffer
    jsonFile.close()  # Close the JSON file
    uploadData['lastUpload'] = type
    # Save our changes to JSON file
    jsonFile = open(jsonPath, "w+")
    jsonFile.write(json.dumps(uploadData))
    jsonFile.close()
    logging.info("Last upload changed to: {}".format(type))

# return what to upload a reel or a post
# 1 is for post
# 2 is for reel
def selectToUploadReelorPost():
    jsonPath = "/home/ash/instaOperator/tmp/uploadData.json"
    type = 0
    if os.path.isfile(jsonPath):
        jsonFile = open(jsonPath, "r")  # Open the JSON file for reading
        uploadData = json.load(jsonFile)  # Read the JSON into the buffer
        jsonFile.close()  # Close the JSON file

        # Making changes in JSON
        if ((uploadData['lastUpload'] == None)):
            type = 1
        elif ((uploadData['lastUpload'] == 0)):
            type = 1
        elif ((uploadData['lastUpload'] == 1)):
            type = 2
        elif ((uploadData['lastUpload'] == 2)):
            type = 1

    else:
        dic = {
            "lastUpload": None
        }
        json_obj = json.dumps(dic)
        with open(jsonPath, "w") as outfile:
            outfile.write(json_obj)
        outfile.close()

    return type

def uploadReel(path):
    try:
        caption = createCaption()
        media = cl.clip_upload(path, caption)
        logging.info("Reel Uploaded from path: {}".format(path))
    except Exception as e:
        logging.warning("Reel Upload Failed Error: {}".format(e))

def uploadPost(path):
    try:
        caption = createCaption()
        media = cl.photo_upload(path, caption)
        logging.info("Post Uploaded from path: {}".format(path))
        movePost(path)
    except Exception as e:
        logging.warning("Post Upload Failed Error: {}".format(e))



logging.basicConfig(filename="log.txt", level=logging.DEBUG, format="%(asctime)s %(message)s")
USERNAME = ""
PASSWORD = ""
path = "~/tmp/dump.json"

# #checking if logion session file exist
if os.path.isfile(path):
    #login file found trying to load session through it
    try:
        cl = Client()
        cl.load_settings(path)
        cl.login(USERNAME, PASSWORD)
        logging.info("Tried to get session from dump.json and got it")
    except Exception as e:
        cl = Client()
        cl.login(USERNAME, PASSWORD)
        cl.dump_settings(path)
        logging.info("Tried to get session from dump.json and exception occurred re saved dump.json")

    while True:
        if connect():
            type = selectToUploadReelorPost()
            logging.info("Selected type: {}".format(type))
            if type == 0:
                continue
            elif type == 1:
                path = getPostPath()
                uploadPost(path)
                changeJSON(type)
                sleepTime = random.randrange(43200, 72000)
                sleepTimeInHour = sleepTime/3600
                logging.info("Post posted sleeping for {} hrs".format(sleepTimeInHour))
                sendMail("Post Uploaded sleeping for {} hrs.".format(sleepTimeInHour))
                time.sleep(sleepTime)
            elif type == 2:
                path = getReelPath()
                uploadReel(path)
                changeJSON(type)
                sleepTime = random.randrange(43200, 72000)
                sleepTimeInHour = sleepTime / 3600
                logging.info("Reel posted sleeping for {} hrs".format(sleepTimeInHour))
                sendMail("Reel Uploaded sleeping for {} hrs.".format(sleepTimeInHour))
                time.sleep(sleepTime)
        else:
            logging.warning("No Internet Sleeping for 10 Min")
            time.sleep(600)

else:
    # login session not found
    logging.info("dump.json not found")
    cl = Client()
    cl.login(USERNAME, PASSWORD)
    logging.info("Logging IN")
    cl.dump_settings(path)
    logging.info("Saved dump.json")
