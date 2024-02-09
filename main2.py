#pip install python-telegram-bot==13.14

from SRT import SRT , SeatType, Adult, Child
import telegram
import time as timer
import argparse
import random


if __name__ == "__main__":
    api_key = ''
    chatId = ''
    bot = telegram.Bot(token=api_key)
    for item in bot.getUpdates():
        print(item)
    
    parser = argparse.ArgumentParser(description='SRT Reservation')
    parser.add_argument('--id', default="")
    parser.add_argument('--pw', default="")
    parser.add_argument('--dep', default="수서")
    parser.add_argument('--arr', default="동대구")
    parser.add_argument('--date', default="20240210")
    parser.add_argument('--start', default="132000")
    parser.add_argument('--end', default="134000")
    parser.add_argument('--iter', default="9999999")
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
    # psg=[Adult()]
    psg=[Adult()]

    for k in range(1, int(iter)+1):
        print("\r"+str(k), end="")
        try:
            # print(srt.reserve(srt.search_train(dep, arr, "20231201", time, time_limit, passengers=psg)[0]))
            reservation = srt.reserve(srt.search_train(dep, arr, date, time, time_limit)[0], passengers=psg)
            bot.sendMessage(chat_id=chatId, text="[SRT]" + str(reservation))
            print(reservation) 
            
            reservation = srt.reserve(srt.search_train(dep, arr, date, time, time_limit)[0], passengers=psg)
            bot.sendMessage(chat_id=chatId, text="[SRT]" + str(reservation))
            print(reservation) 
            
            reservation = srt.reserve(srt.search_train(dep, arr, date, time, time_limit)[0], passengers=psg)
            bot.sendMessage(chat_id=chatId, text="[SRT]" + str(reservation))
            print(reservation) 
            
        except:
            timer.sleep(random.uniform(0.0, 2.0))
            continue
    bot.sendMessage(chat_id=chatId, text="[SRT] Reservation finished")
