import sys
import socket
import PySimpleGUI as sg

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

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
        port = int(values[1])
        #print(socket.gethostbyname( host ))
        #address = host + ":" + port

        print('# Getting remote IP address') 


        # Connect to remote server
        print('# Connecting to server, ' + host)
        client.connect((host , port))
        # Send data to remote server

         # Receive data
        data = client_socket.recv(1024).decode()  # receive response
        print('Received from server: ' + data) 

        print('# Sending data to server')
        request = "GET / HTTP/1.0\r\n\r\n"

        try:
            data = input('On')
            client.send(data.encode())
            print('# on')
        except socket.error:
            print ('Send failed')
            sys.exit()

       
    if event == "Apagar":
        print("Desconectar ", values)
        try:
            data = input('Off')
            client.sendall(data.encode())
            print('# off')
        except socket.error:
            print ('Send failed')
            sys.exit()
        
        #sio.disconnect()
      
window.close()