#pip install python-telegram-bot==13.14

from SRT import SRT , SeatType, Adult, Child
import telegram
import time as timer

if __name__ == "__main__":
    api_key = ''
    chatId = ''
    bot = telegram.Bot(token=api_key)
    for item in bot.getUpdates():
        print(item)


    srt = SRT("", "")
    dep = '수서'
    arr = '동대구'
    # date = '20231005'
    date = '20230928'
    time = '100000'
    time_limit = '120000'
    
    # trains = srt.search_train('수서', '대전', '20221122', '000000')
    seatType = '일반실'

    count = 0 
    while True:
        trains = srt.search_train(dep, arr, date, time, time_limit)
        # trains = '[[SRT 349] 09월 26일, 수서~동대구(16:21~17:58) 특실 예약가능, 일반실 매진, 예약대기 불가능, [SRT 393] 09월 26일, 수서~동대구(16:34~18:20) 특실 예약가능, 일반실 매진, 예약 대기 불가능, [SRT 355] 09월 26일, 수서~동대구(17:30~19:08) 특실 매진, 일반실 예약가능, 예약대기 불가능, [SRT 379] 09월 26일, 수서~동대구(22:40~00:25) 특실 매진, 일반실 예 약가능, 예약대기 불가능]'
        count += 1
        print("\r"+str(count), end="")
        
        for i in range(0, len(trains)):
            print(trains[i])
        j = 0
        for j in range(0, len(trains)):
            if seatType in str(trains[j]):
                try:
                    reservation = srt.reserve(trains[j])
                    print(reservation)
                    bot.sendMessage(chat_id=chatId, text=str(reservation))
                    continue
                except:
                    continue
        timer.sleep(2)

