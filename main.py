#pip install python-telegram-bot==13.14
#python ./main.py --id 010-4442-5552 --pw Dighwjdgh3# --dep 수서 --arr 동대구 --date 20230929 --start 100000 --end 120000 --iter 3 --seat 일반실
from SRT import SRT , SeatType, Adult, Child
import telegram
import time as timer
import argparse

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
    parser.add_argument('--end', default="120000")
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

    # srt = SRT("010-4442-5552", "Dighwjdgh3#")
    # dep = '수서'
    # arr = '동대구'
    # date = '20230929'
    # time = '100000'
    # time_limit = '120000'
    
    # trains = srt.search_train('수서', '대전', '20221122', '000000')

    for k in range(1, int(iter)+1):
        trains = srt.search_train(dep, arr, date, time, time_limit)
        # trains = '[[SRT 349] 09월 26일, 수서~동대구(16:21~17:58) 특실 예약가능, 일반실 매진, 예약대기 불가능, [SRT 393] 09월 26일, 수서~동대구(16:34~18:20) 특실 예약가능, 일반실 매진, 예약 대기 불가능, [SRT 355] 09월 26일, 수서~동대구(17:30~19:08) 특실 매진, 일반실 예약가능, 예약대기 불가능, [SRT 379] 09월 26일, 수서~동대구(22:40~00:25) 특실 매진, 일반실 예 약가능, 예약대기 불가능]'
        print("\r"+str(k), end="")
        
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
        # timer.sleep(1)

