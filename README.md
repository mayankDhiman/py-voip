### Implementation of Voice over Internet Protocol (VOIP) in Python3
It is an implementation of Voice over Internet Protocol in Python3.

### Running instructions
- Create a virtual environment, using `python -m venv env`
- Install all the dependencies using `pip install -r requirements.txt`
- Start the server using `python server.py`
- Start the client using `python client.py`, this should start a window with a _Push_ button to record the voice. 
- Push the button in window, speak something, your voice should be audible on speaker where the server is located. 
- Considering the client & server will run on the same machine, I have used `socket.getHostName()` method, if using on different machines, we are supposed to put the address of the host available to both machines

### Keywords
Networking, Internet Protocols

### Future improvements: 
- Develop a Flask & Angular based web app.
