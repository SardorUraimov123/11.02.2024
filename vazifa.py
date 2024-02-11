import threading
import os

def unli_calc(f_name):
    unlilar = "A,a,E,e,I,i,U,u,O,o,U,u"
    with open(f_name, 'r') as f:
        cnt = f.read()
        unli_c = sum(1 for char in cnt if char in unlilar)
        print(f"Fayl:{f_name}, faildagi unlilar soni : {unli_c}")


def mn():
    txt_fs = [f for f in os.listdir() if f.endswith(".txt")]
    thread = []
    for txt_f in txt_fs:
        thrid = threading.Thread(target=unli_calc, args=(txt_f,))
        thread.append(thrid)
        thrid.start()

    for thrid in thread:
        thrid.join()

if __name__ == "__main__":
    mn()