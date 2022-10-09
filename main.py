class station:
    buses = {1: "from Rafah to Khan", 2: "from Gaza to Bethanon", 3: "from alqoda to gaza ", 4: "from jenen to rafah"}
    seats_1 = {1: 'free', 2: 'book', 3: 'book', 4: 'free', 5: 'free', 6: 'free'}
    seats_2 = {1: 'book', 2: 'free', 3: 'book', 4: 'book', 5: 'free', 6: 'book'}
    seats_3 = {1: 'free', 2: 'free', 3: 'book', 4: 'book', 5: 'book', 6: 'free'}
    seats_4 = {1: 'book', 2: 'free', 3: 'book', 4: 'book', 5: 'book', 6: 'free'}

    def __init__(self , Fname , Lname, Id, phoneNum):
        self.Fname = Fname
        self.Lname = Lname
        self.Id = Id
        self.phoneNum = phoneNum


    def seat(self,buses,seats_1,seats_2,seats_3,seats_4,First_name,Lastname,Id,phone_nu):
        print("choose num of these buses")
        print(buses)
        x=int(input(" your bus is  = "))
        again=0
        while again==0:
            if x == 1:
                print("this is the list of seats in your bus")
                print(seats_1)
                y = int(input("choose your seat num"))
                if seats_1[y] == "free":
                    seats_1[y] = "book by "+First_name
                    print(First_name,Lastname, "id = ",Id,"massage to ",phone_nu,"you are successfully book the seat num = ", y)
                    print("this a new list of seat", seats_1)
                    again = 1
                else:
                    print("sorry this seat is book choose another one")
                    again = 0
            elif x == 2:
                print("this is the list of seats in your bus")
                print(seats_2)
                y = int(input("choose your seat num"))
                if seats_2[y] == "free":
                    seats_2[y] = "book by "+First_name
                    print(First_name,Lastname, "id = ",Id,"massage to ",phone_nu,"you are successfully book the seat num = ", y)
                    print("this a new list of seat", seats_2)
                    again = 1
                else:
                    print("sorry this seat is book choose another one")
                    again = 0
            elif x == 3:
                print("this is the list of seats in your bus")
                print(seats_3)
                y = int(input("choose your seat num"))
                if seats_3[y] == "free":
                    seats_3[y] = "book by "+First_name
                    print(First_name,Lastname, "id = ",Id,"massage to ",phone_nu,"you are successfully book the seat num = ", y)
                    print("this a new list of seat", seats_3)
                    again = 1
                else:
                    print("sorry this seat is book choose another one")
                    again = 0
            elif x == 4:
                print("this is the list of seats in your bus")
                print(seats_4)
                y = int(input("choose your seat num"))
                if seats_4[y] == "free":
                    seats_4[y] = "book by "+First_name
                    print(First_name,Lastname, "id = ",Id,"massage to ",phone_nu,"you are successfully book the seat num = ", y)
                    print("this a new list of seat", seats_4)
                    again = 1
                else:
                    print("sorry this seat is book choose another one")
                    again = 0


f=input("enter your first name")
g=input("enter your last name")
h=int(input("enter your Id num"))
i=int(input("enter your phone num"))
opj=station(f,g,h,i)
print("welcome", f,g, "Id=  ", h,"phone num = ",i)
a=opj.buses
b=opj.seats_1
c=opj.seats_2
d=opj.seats_3
e=opj.seats_4


opj.seat(a,b,c,d,e,f,g,h,i)