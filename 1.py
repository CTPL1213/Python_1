import os
import datetime
import sys

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
    os.chdir('../')
    date=str(datetime.datetime.now())
    date=date.split()
    date='_'.join(date)
    os.rename('Results','Results_'+date)
    os.system('cp -R /var/lib/jenkins/workspace/Demo/Results_2022-01-06_16\:51\:47.820563/  /home/tuser/Desktop/Results')
    print('Success..!!!')
    
    
