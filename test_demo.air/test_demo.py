from airtest.core.api import *


PKG = "com.example.rthk_flutter_app"

stop_app(PKG)
home()

start_app(PKG)
sleep(5)

swipe(Template(r"tpl1607756997847.png", record_pos=(0.057, 0.678), resolution=(720, 1560)), vector=[-0.0524, -0.6082])

touch(Template(r"tpl1607757031169.png", record_pos=(0.058, 0.529), resolution=(720, 1560)))

touch(Template(r"tpl1607757053692.png", record_pos=(0.007, -0.694), resolution=(720, 1560)))

touch(Template(r"tpl1607757067934.png", record_pos=(0.381, -0.776), resolution=(720, 1560)))

touch(Template(r"tpl1607757104291.png", record_pos=(-0.343, 1.014), resolution=(720, 1560)))

text("test")

touch(Template(r"tpl1607757163686.png", record_pos=(0.408, 0.222), resolution=(720, 1560)))

touch(Template(r"tpl1607757182687.png", record_pos=(-0.418, -0.912), resolution=(720, 1560)))

touch(Template(r"tpl1607757194400.png", record_pos=(-0.414, -0.912), resolution=(720, 1560)))

swipe(Template(r"tpl1607757226044.png", record_pos=(0.061, -0.588), resolution=(720, 1560)), vector=[-0.0025, 0.6578])

touch(Template(r"tpl1607757242660.png", record_pos=(-0.419, -0.915), resolution=(720, 1560)))

touch(Template(r"tpl1607757254486.png", record_pos=(-0.258, 0.294), resolution=(720, 1560)))

touch(Template(r"tpl1607757263711.png", record_pos=(-0.418, -0.912), resolution=(720, 1560)))

touch(Template(r"tpl1607757280462.png", record_pos=(0.436, -0.915), resolution=(720, 1560)))


log("Test OK")

sleep(2)
stop_app(PKG)

