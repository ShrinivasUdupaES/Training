class destination:
    __count=0
    li = ["cost","distance","rating","description"]
    places = ["ooty","shimla","yelagiri"]
    costs = [5000,10000,4000]
    ratings  =[3.5,4.2,3]
    descriptions = ["abc","xyz","lmn"]
    distance = [400,1500,200]

    def __new__(cls, *args, **kwargs):
        if cls.__count<=2:
            cls.__count+=1
            return object.__new__(cls)

    def __init__(self,place_name,no_of_people):
        self.place_name=place_name
        self.no_of_people=no_of_people

    def display(self):
        y=self.no_of_people
        cost=(list(map(lambda x:x*y,__class__.costs)))
        d=list(zip(cost,__class__.distance,__class__.ratings,__class__.descriptions))
        dic=dict(zip(__class__.places,d))
        # print(dic)
        # print(dic[self.place_name])
        for k,v in dic.items():
            if k == self.place_name:
                print("Cost : {0}".format(v[0]))
                print("Distance : {0}".format(v[1]))
                print("Rating : {0}".format(v[2]))
                print("Description : {0}".format(v[3]))



place_name = input("Enter the place name(ooty,shmila,yelagiri) : ")
no_of_people = int(input("Enter the number of people : "))
person = destination(place_name,no_of_people)
person.display()
# li=["cost","distance","rating","description"]
# places=["ooty","shimla","yelagiri"]
# costt=[10000,20000,8000]
# ratingg=[3.5,4.2,3]
# descriptionn=["abc","xyz","lmn"]
# dist=[400,1500,200]
# d=list(zip(costt,dist,ratingg,descriptionn))
# dic=dict(zip(places,d))
# person1.display(dic)
# for x in places:
#     dic[x]={}
# print(dic)
# for x in dic:
#     for i in range(1,4):
#         dic[x]["cost"]=costt[i]
#         dic[x]["distance"]=dist[i]

# print(dic)

