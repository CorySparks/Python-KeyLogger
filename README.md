# Python-KeyLogger
Writen in Python 2.7.10. For educational use only.

# Logger

The logger grabes every keystroke and applys them to a text file on the victims computer, as well as pushed to a server
to store the keystrokes if we are unable to acquire the text file.

# Broker

The broker keeps the logger alive using Deamon, even if the victim would try and kill the program via task manager or some other
form of that. The broker is stored in the startup file and changed to x.exe, from executing the payload.

# Payload

The payload would have to be injected manually as of right now. Try and store the payload in a folder that no one ever looks in, I store mine in `C:/Users/"+user+"/.idlerc/`. The payload downloads Python(2.7.10), the logger while changing the name to x.pyw, and the broker but stores that in the startup file.
