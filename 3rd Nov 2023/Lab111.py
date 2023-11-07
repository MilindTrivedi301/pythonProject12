class Myclass:

    def print_my_name_with_last_name(self,name, last_name, age):
        print("You name is -> " + name, last_name, age)


pramod_obj_ref = Myclass()
pramod_obj_ref.print_my_name_with_last_name("Milind", "Trivedi", 24)


#-----------------------------------------------------------------
#name = None

#    def print_my_name(self):
#        print("Your name is ->" + self.name)

#    name_obj_ref = Myclass()
#    name_obj_ref.name = "Milind"
#    name_obj_ref.print_my_name()