import sys
import socket
import socketio
import PySimpleGUI as sg

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()
    
sio = socketio.Client()
print('Socket Created')

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Ingresa los datos para conectar')],
            [sg.Text('Ingresa la direccion IP'), sg.InputText()],
            [sg.Text('Ingresa el puerto'), sg.InputText()],
            [sg.Button('Encender'), sg.Button('Apagar'),sg.Cancel()],]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Encender':
        print("Conectar ", values)
        host = values[0]
        port = values[1]
        #print(socket.gethostbyname( host ))
        address = host + ":" + port

        if sio.sid:
            print("Ya hay una conexion")
        else:
            print('# Connecting to server, ' + address)
            sio.connect(address)
            data = sio.recv(19)
            print (sys.stderr, 'recibido "%s"' % data)
        
        
        print('my sid is', sio.sid)
        sio.emit('message', {'Action': 'on'})
       
    if event == "Apagar":
        print("Desconectar ", values)
        sio.emit('message', {'Action': 'off'})
        
        #sio.disconnect()
      
window.close()