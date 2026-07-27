from opps_project import chatbook
user1 = chatbook()
print(user1.id)

chatbook.set_id(10)
user2 = chatbook()
print(user2.id)

user3 = chatbook() 
print(user3.id)



# print(user1.get_name())
# user1.set_name("Sam")
# print(user1.get_name())
# function vs method below

#lst = [1,2,3]

# # function
# a1 = len(lst)
# print(a1)

# # method
# user1 = chatbook()
# user1.send_msg()