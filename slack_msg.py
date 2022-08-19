import requests


#### botToken, Channel setting ####
myToken = "token"
channelName = "#channel"

#### massage setting ####
msgAlarm = "Hi"



class SlackMsg :
    def post_message(self, token, channel, text):
        response = requests.post("https://slack.com/api/chat.postMessage",
            headers={"Authorization": "Bearer "+token},
            data={"channel": channel,"text": text}
        )
        print(response)



if __name__ == "__main__":
    msg = SlackMsg()
    msg.post_message(myToken, channelName, msgAlarm)


