#pip install python-telegram-bot==13.14

from SRT import SRT , SeatType, Adult, Child
import telegram
import time as timer
import argparse
import random

if __name__ == "__main__":
    api_key = '5957545379:AAFAHTqrMAqMAWUsD9EkT3XvLcsu0snQgRV'
    chatId = '5517769457'
    bot = telegram.Bot(token=api_key)
    for item in bot.getUpdates():
        print(item)
    
    parser = argparse.ArgumentParser(description='SRT Reservation')
    parser.add_argument('--id', default="")
    parser.add_argument('--pw', default="")
    parser.add_argument('--dep', default="수서")
    parser.add_argument('--arr', default="동대구")
    parser.add_argument('--date', default="20230929")
    parser.add_argument('--start', default="090000")
    parser.add_argument('--end', default="140000")
    parser.add_argument('--iter', default="1000")
    parser.add_argument('--seat', default="일반실")
    args = parser.parse_args()
    print(args)

    srt = SRT(args.id, args.pw)
    dep = args.dep
    arr = args.arr
    date = args.date
    time = args.start
    time_limit = args.end
    iter = args.iter
    seatType = args.seat

    for k in range(1, int(iter)+1):
        
        try: 
            trains = srt.search_train(dep, arr, date, time, time_limit)
            # print(trains)
        except:
            timer.sleep(random.uniform(0.0, 2.0))
            trains = srt.search_train(dep, arr, date, time, time_limit)
            # continue 
        print("\r"+str(k), end="")
        
        for i in range(0, len(trains)):
            print(trains[i])
        j = 0
        for j in range(0, len(trains)):
            if seatType in str(trains[j]):
                try:
                    reservation = srt.reserve(trains[j])
                    print(reservation)
                    bot.sendMessage(chat_id=chatId, text="[SRT]" + str(reservation))
                    continue
                except:
                    continue
        timer.sleep(random.uniform(0.0, 2.0))
    bot.sendMessage(chat_id=chatId, text="[SRT] Reservation finished")
    
