import os


directory = 'C:/Users/TONYE OWUNARI'
check_file = str(input('Check what folder: '))

def file(directory, check_file):
    for i in os.listdir(directory):
        if i == check_file:
            directory += '/' + check_file
            print(os.listdir(directory))
            next_check = str(input('Check what folder: '))

            for j in os.listdir(directory):
                if j == next_check:
                    directory += '/' + next_check                    
                    for k in os.listdir(directory):
                        print(k)
                    play = str(input('Play what: '))                    
                    directory += '> "' + play + '"'
                    os.path = directory
                            

                    

                        



file(directory, check_file)

