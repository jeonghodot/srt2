#pip install python-telegram-bot==13.14

from SRT import SRT ,SeatType, Adult, Child
import telegram
import time as timer
import argparse
import random
import os
import sys
import subprocess

def restart():
    python_executable = sys.executable
    script_path = sys.argv[0]
    
    subprocess.run([python_executable, script_path])
    
if __name__ == "__main__":
    api_key = ''
    chatId = ''
    bot = telegram.Bot(token=api_key)
    for item in bot.getUpdates():
        print(item)
    
    parser = argparse.ArgumentParser(description='SRT Reservation')
    parser.add_argument('--id', default="")
    parser.add_argument('--pw', default="")
    parser.add_argument('--dep', default="동대구")
    parser.add_argument('--arr', default="수서")
    parser.add_argument('--date', default="20240220")
    parser.add_argument('--start', default="100000")
    parser.add_argument('--end', default="110000")
    parser.add_argument('--iter', default="9999999")
    parser.add_argument('--seat', default=SeatType.SPECIAL_ONLY)
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
    psg=[Adult()]
    # psg=[Adult()]

    seatType=SeatType.SPECIAL_ONLY
    # 1 SeatType.GENERAL_FIRST : 일반실 우선
    # 2 SeatType.GENERAL_ONLY : 일반실만
    # 3 SeatType.SPECIAL_FIRST : 특실 우선
    # 4 SeatType.SPECIAL_ONLY : 특실만
    # special_seat: SeatType = SeatType.GENERAL_FIRST


    for k in range(1, int(iter)+1):
        print("\r"+str(k), end="")
        try:
            # print(srt.search_train(dep, arr, date, time, time_limit))
            for i in range(3) :
                reservation = srt.reserve(srt.search_train(dep, arr, date, time, time_limit)[0], special_seat=seatType, passengers=psg,)
                bot.sendMessage(chat_id=chatId, text=str(reservation))
                print(reservation) 
            
            # reservation = srt.reserve(srt.search_train(dep, arr, date, time, time_limit)[0], passengers=psg)
            # bot.sendMessage(chat_id=chatId, text=str(reservation))
            # print(reservation) 
            
            # reservation = srt.reserve(srt.search_train(dep, arr, date, time, time_limit)[0], passengers=psg)
            # bot.sendMessage(chat_id=chatId, text=str(reservation))
            # print(reservation) 
            
        except IndexError as e:
            timer.sleep(random.uniform(0.0, 2.0))
            continue
        except Exception as f:
            print(f)
            #print("script restarted")
            restart()
            continue
        
    bot.sendMessage(chat_id=chatId, text="[SRT] Reservation finished")
