import requests

#### botToken, Channel setting ####
myToken = "xoxb-3919741179778-3978768326241-RIzqvlzHd7U5yf89JHH3Hzfo"
channelName = "#srt-자동-예약-시스템"

#### massage setting ####
msgAlarm = "srt macro"



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


