#funciones que le pertenecen a un objeto se llaman metodos methods
class User :    
    def __init__(self, user_email,name,password,current_job_title):
        self.email = user_email
        self.name= name
        self.password =password
        self.current_job_title =current_job_title

    def change_password(self,new_password):
    self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def add_new_skill():

user("amy@gmail.com","ami sauria","ami666","developer")
