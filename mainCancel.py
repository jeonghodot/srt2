
from SRT import SRT , SeatType, Adult, Child

if __name__ == "__main__":
    
    srt = SRT("", "")
    
    reservations = srt.get_reservations()
    print(reservations)

    for i in range(0, len(reservations)):
        srt.cancel(reservations[i])

    reservations = srt.get_reservations()
    print(reservations)
