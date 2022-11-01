import pytest
import System


username = 'calyam'
password =  '#yeet'
username2 = 'hdjsr7'
username3 = 'yted91'
studentUser = 'akend3'
studentPass = '123454321'
course = 'cloud_computing'
course2 = 'software_engineering'
assignment = 'assignment1'
profUser = 'goggins'
profPass = 'augurrox'



def test_login(grading_system):                 #test1 pass
    grading_system.login('yted91', 'imoutofpasswordnames')

def test_check_password(grading_system):        #test2 pass
    test = grading_system.check_password(username,password)
    test2 = grading_system.check_password(username,'#yeet')
    test3 = grading_system.check_password(username,'#YEET')
    test4 = grading_system.check_password(username, '#YeEt')
    test5 = grading_system.check_password(username, '#yEeT')
    test6 = grading_system.check_password(studentUser, studentPass)
    if test == test3 or test2 == test3 or test2 == test3 or test2 == test4:
        assert False
    if test != test2:
        assert False
    if test == test4:
        assert False
    if test == test5:
        assert False
    if test == test6:
        assert False
    

def test_change_grade(grading_system):          #test3 fail
    grading_system.login('cmhbf5', 'bestTA')
    grading_system.usr.change_grade(username3, course2, '20')
    

def test_create_assignment(grading_system):     #test4 pass
    grading_system.login(profUser, profPass)
    grading_system.usr.create_assignment('biology', '2/2/22', course2)

def test_add_student(grading_system):           #test5 fail
    grading_system.login(profUser,profPass)
    grading_system.usr.add_student('akend3', course2)

def test_drop_student(grading_system):          #test6 pass
    grading_system.login(profUser,profPass)
    grading_system.usr.drop_student('akend3', 'databases')

def test_submit_assignment(grading_system):     #test7 pass
    grading_system.login('hdjsr7','pass1234')
    grading_system.usr.submit_assignment(course2, 'assignment2', 'genesAndSuch', '9/9/20')

def test_check_ontime(grading_system):    #test8 fail
    grading_system.login('yted91','imoutofpasswordnames')
    test = 'false'
    test2 = grading_system.usr.check_ontime('2/5/20', '2/1/20')
    if test != test2:
        assert False

def test_check_grades(grading_system):      #test9 fail
    grading_system.login('hdjsr7','pass1234')
    grading_system.usr.check_grades(course)
    
def test_view_assignments(grading_system):  #test10 pass
    grading_system.login('hdjsr7','pass1234')
    grading_system.usr.view_assignments(course)

# - - - - - - Custom Checks

def test_Staff_Dont_Look(grading_system): #Custom check #1 fail, cannot view grade without error
    grading_system.login('cmhbf5', 'bestTA')
    grading_system.usr.check_grades(username3, course)
   

def test_Canvas_Never_Lies(grading_system):    #Custom check #2, always returns true regardless of state
    grading_system.login('hdjsr7','pass1234')
    test = 'false'
    test2 = grading_system.usr.check_ontime('2/5/20', '2/6/20')
    if test != test2:
        assert False

def test_Not_My_Prof(grading_system):           #Custom check #3, goggins does not teach the class getting dropped
    grading_system.login(profUser,profPass)
    grading_system.usr.drop_student('akend3', 'comp_sci')
    if True:
        assert False

def test_Extra_Credit(grading_system):     #Custom check #4, no bounds check on the due date string
    grading_system.login('cmhbf5', 'bestTA')
    grading_system.usr.create_assignment('business101', '2/2/2222222222222222',course2)
    if True:
        assert False

def test_Have_Fun_Kiddos(grading_system):     #Custom check #5, There is no TA for comp_sci
    grading_system.login('cmhbf5', 'bestTA')
    grading_system.usr.create_assignment('freepoints', '2/2/22','comp_sci')
    if True:
        assert False


# - - - - - - Fixtures

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

@pytest.fixture
def TA():
    grading_system.login('cmhbf5', 'bestTA')
    Ta = grading_system.usr
    return Ta

@pytest.fixture
def checking_grade():
    grading_system.login(profUser, profPass)
    Prof = grading_system.usr
    return Prof