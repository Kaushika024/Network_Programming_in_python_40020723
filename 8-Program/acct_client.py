import json
import socket


c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 20202
c.connect((host,port))

class Account:
    def __init__(self, number, name, branch):
        self.number = number
        self.name = name
        self.branch = branch

class Employee:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

class Box:
    def __init__(self, colour, weight, height):
        self.colour = colour
        self.weight = weight
        self.height = height

class Customer:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

if __name__ == "__main__":

    a1 = Account("625468845287", "saving", "Canara")
    a2 = Account("638465792548", "saving", "Kvb")

    e1 = Employee("40020719", "Sowmiya", "22")
    e2 = Employee("40020609", "Pavithra", "22")

    b1 = Box("brown", "60", "5.9")
    b2 = Box("black", "47", "5.7")

    c1 = Customer("Sindhu", "40020500", "21")
    c2 = Customer("Kavya", "40040698", "24")


    jsonstr1 = json.dumps(a1.__dict__)
    jsonstr2 = json.dumps(a2.__dict__)
    jsonstr3 = json.dumps(e1.__dict__)
    jsonstr4 = json.dumps(e2.__dict__)
    jsonstr5 = json.dumps(b1.__dict__)
    jsonstr6 = json.dumps(b2.__dict__)
    jsonstr7 = json.dumps(c1.__dict__)
    jsonstr8 = json.dumps(c2.__dict__)

    print('Json convertion')
    print('Sent to server')
    print('Decoding will be on server end')

    data1 = jsonstr1
    c.send(data1.encode('utf-8'))

    data2 = jsonstr2
    c.send(data2.encode('utf-8'))

    data3 = jsonstr3
    c.send(data3.encode('utf-8'))

    data4 = jsonstr4
    c.send(data4.encode('utf-8'))

    data5 = jsonstr5
    c.send(data5.encode('utf-8'))

    data6 = jsonstr6
    c.send(data6.encode('utf-8'))

    data7 = jsonstr7
    c.send(data7.encode('utf-8'))

    data8 = jsonstr8
    c.send(data8.encode('utf-8'))


c.close()
