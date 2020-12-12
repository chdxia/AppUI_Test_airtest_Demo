from airtest.core.api import *


PKG = "com.example.rthk_flutter_app"

stop_app(PKG)
home()

start_app(PKG)
sleep(5)

touch(Template(r"tpl1607741403390.png", record_pos=(0.057, -0.651), resolution=(720, 1560)))

touch(Template(r"tpl1607741494244.png", record_pos=(0.008, -0.692), resolution=(720, 1560)))

touch(Template(r"tpl1607741541458.png", record_pos=(0.375, -0.774), resolution=(720, 1560)))

touch(Template(r"tpl1607741561759.png", record_pos=(-0.417, -0.908), resolution=(720, 1560)))

touch(Template(r"tpl1607741582928.png", record_pos=(-0.421, -0.915), resolution=(720, 1560)))

swipe(Template(r"tpl1607741856846.png", record_pos=(0.062, 0.465), resolution=(720, 1560)), vector=[-0.0399, -0.4752])

touch(Template(r"tpl1607741892844.png", record_pos=(-0.422, -0.915), resolution=(720, 1560)))

touch(Template(r"tpl1607742021361.png", record_pos=(-0.256, 0.296), resolution=(720, 1560)))

touch(Template(r"tpl1607742032690.png", record_pos=(-0.417, -0.911), resolution=(720, 1560)))

touch(Template(r"tpl1607742046493.png", record_pos=(0.432, -0.91), resolution=(720, 1560)))

log("Test OK")

sleep(2)
stop_app(PKG)

