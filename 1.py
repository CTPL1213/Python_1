import os
import datetime
os.system('cd /home/tuser/Desktop/')
def makedir(dir_name):
    if os.path.isdir(dir_name):
        os.chdir(os.path.join(os.getcwd(),dir_name))
    else:
        
        os.mkdir(os.path.join(os.getcwd(),dir_name))

        os.chdir(os.path.join(os.getcwd(),dir_name)) 

def createfile(file_name):
    date=str(datetime.datetime.now())
    date=date.split()
    date='_'.join(date)
    file_name+=date
    with open(os.path.join(os.getcwd(),file_name+'.txt'),'w'):
        pass
if __name__=='__main__':
    print(os.getcwd())
    makedir('Results')
    createfile('test_11')
    print('Python')
