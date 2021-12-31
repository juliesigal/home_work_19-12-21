from Kita import Kita
from db_config import local_session, create_all_entities
from Students import Students
from Db_repo import DbRepo

# create tables
create_all_entities()

repo = DbRepo(local_session)

k1 = Kita(floor=2, num_of_student=15, class_avg=84.5)
k2 = Kita(floor=3, num_of_student=18, class_avg=79.5)
kita_ls = [k1, k2]
#repo.add_all(kita_ls)

st1 = Students(fname='Liron', lname='Cohen', grade_avg=83.9, kita_id=1)
st2 = Students(fname='Daniel', lname='Liss', grade_avg=84, kita_id=2)
st_list = [st1, st2]

#repo.add_all(st_list)

print(repo.get_by_condition(Students, lambda query: query.filter(Kita.id == 2).all()))
print(repo.get_by_condition(Students, lambda query: query.filter(Kita.id == 1).all()))


