from gopigo import *

enable_encoders()
enable_servo()

target = 2

enc_tgt(1, 1, 2)
print target
set_speed(180)
left_rot()
time.sleep(5)

enc_tgt(1, 1, 2)
print target
set_speed(180)
right_rot()
time.sleep(5)

enc_tgt(1, 1, 2)
print target
set_speed(180)
left_rot()
time.sleep(5)

enc_tgt(1, 1, 2)
print target
set_speed(180)
right_rot()
time.sleep(5)