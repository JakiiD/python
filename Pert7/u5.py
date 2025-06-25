import threading
from threading import Thread
import time

class restoran:
    def __init__(self, Andi, Budi, Citra):
        self.Andi = Andi
        self.Budi = Budi
        self.Citra = Citra

    def andii(self):
        print('Penumpang Andi sedang checkin ke tujuan {}'.format(self.Andi))
        print('Penumpang Andi sedang boarding ke pesawat tujuan {}'.format(self.Andi))

    def budii(self):
        print('Penumpang Budi sedang checkin ke tujuan {}'.format(self.Budi))
        print('Penumpang Budi sedang boarding ke pesawat tujuan {}'.format(self.Budi))

    def citraa(self):
        print('Penumpang Citra sedang checkin ke tujuan {}'.format(self.Citra))
        print('Penumpang Citra sedang boarding ke pesawat tujuan {}'.format(self.Citra))

    def run(self):
        self.andii()
        self.budii()
        self.citraa()

if __name__ == '__main__':
    start = time.perf_counter()
    Andis = [
        'Jakarta',
        'Surabaya',
        'Bali',
    ]
    Budis = [
        'Jakarta',
        'Surabaya',
        'Bali',
    ]
    Citras = [
        'Jakarta',
        'Surabaya',
        'Bali',
    ]

    thread_list = []
    for Andi in Andis:
        for Budi in Budis:
            for Citra in Citras:
                t = Thread(target=restoran(Andi, Budi, Citra).run)
                t.start()
                time.sleep(1)
                thread_list.append(t)
                break
    for thread in thread_list:
        thread.join()

    finish = time.perf_counter()
    print('Waktu Total : ', finish - start)
