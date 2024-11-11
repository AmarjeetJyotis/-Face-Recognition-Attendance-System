import os
from random import randint

# Set the actual path to your GitHub repository
repository_path = 'S:\\graph_filler'
os.chdir(repository_path)

# Loop through each day in the past year
for i in range(1, 365):
    # Create a random number of commits for each day
    for j in range(0, randint(1, 10)):
        # Set the date format correctly
        d = f'{i} days ago'
        
        # Write to a file to simulate changes
        with open('file.txt', 'a') as file:
            file.write(d + '\n')
        
        # Add file to git
        os.system('git add file.txt')
        
        # Commit with the specified date
        os.system(f'git commit --date="{d}" -m "commit"')

# Push to the main branch
os.system('git push -u origin main')
