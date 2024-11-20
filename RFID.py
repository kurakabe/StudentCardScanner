from pirc522 import RFID
from time import sleep
reader = RFID()
keys= list()
key_read = True
try:
    while True:
        reader.wait_for_tag()
        error, tag_type = reader.request()
        if not error:
            error, uid = reader.anticoll()
            if not error:
                if len(keys) > 0:
                    for key in keys:
                        if key == uid:
                            key_read = False
                            break
                        else:
                            key_read = True
                else:
                    key_read = True
                if key_read:
                    keys.append(uid)
                    print(uid)
                    reader.stop_crypto()
                else:
                    print("#")
            sleep(0.1)
except KeyboardInterrupt:
    print("script end")
finally:
    reader.cleanup()