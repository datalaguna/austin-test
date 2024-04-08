import datetime
import os
import uuid
import datetime
import random

number_of_files = 5
number_of_directories = 5

directory = "/dist/queue"

def createFile(file_path,content):
  # Write the content to the file
    with open(file_path, "w") as file:
        file.write(content)

    print(f"File created: {file_name}")

for j in range(1, number_of_directories+1):
    new_uuid = uuid.uuid4()
    directory_name = f"{new_uuid}"
    dir_path = os.path.join(directory, directory_name)
    os.mkdir(dir_path)

    file_name = "ToBeProcessedBefore"   

    # Get today's date
    today = datetime.date.today()

    random_date = datetime.datetime.now() + datetime.timedelta(days=random.randint(-1, 1))
    random_time = datetime.time(random.randint(0, 23), random.randint(0, 59))
    random_datetime = datetime.datetime.combine(random_date.date(), random_time)

    # Convert datetime to string
    content = random_datetime.strftime("%Y-%m-%d %H:%M:%S")

    file_path = os.path.join(dir_path, file_name)
    createFile(file_path,content)
    
    for i in range(1, number_of_files + 1):

        new_uuid = uuid.uuid4()
        file_name = f"{new_uuid}.txt"

        file_path = os.path.join(dir_path, file_name)            
      
        content =""
        content += f"File Name: {file_name}\n"
        content += f"File Number: {i}\n"
        content += f"Generated on: {datetime.datetime.now()}\n"
        content += "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        createFile(file_path,content)      

print("Mock files generation completed.")


