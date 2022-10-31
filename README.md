# CS361_Microservice

Communication Contract:

a) How to REQUEST data: a request is made to the microservice via ZeroMQ. Connect to my server, send either addition, multiplication, or subtraction as STRINGS
to this server. Example call: 

Connect to the server


![image](https://user-images.githubusercontent.com/91137143/199122924-45a876b7-cc85-4b1c-94f4-5109f0489ccc.png)


Send a string to the server


![image](https://user-images.githubusercontent.com/91137143/199122952-35ca1a11-eb83-4c28-8766-9714140a02c5.png)



b) How to RECEIVE data: Once a request as been made, the requester will receive a JSON object containing the 5 random math questions and the answer to each question. 

Example receive:

While connected to the server, 

![image](https://user-images.githubusercontent.com/91137143/199123540-613e1420-a360-4bd2-b5b9-95b20a8e1b1f.png)


JSON Format example:

![image](https://user-images.githubusercontent.com/91137143/199123696-1fa4705d-4d4a-4c24-a6e7-0a22ecadeb20.png)


UML Diagram:

![image](https://user-images.githubusercontent.com/91137143/199123805-013be388-0ab1-4c9a-bc2d-0cc90e15dfb9.png)



