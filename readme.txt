set up venv : 
1 : python3 -m venv myvenv   <- create venv     
2 : myvenv\Scripts\activate  <- activate venv 
2.a : when opening vscode, ou et enter interpretor path , ignore it 
3 : python manage.py runserver <- make sure your path is at clbackend

start a project : 
1: cd to clbackend 
2: make sure you are in venv and type python maange.py starapp api <- this create api folder

about django: 
django use so called ORM (object relational mapping )
views handles sql 
urls handle interaction between frontend and backend

git tutorial : 
sign in to git -> git init -> git config --global user.name "Your Name" , git config --global user.email you@example.com
git status -> git chekcout -> git add all . -> git status -> git commit -m "My Django Girls app, first commit" 
-> git remote add origin https://github.com/<your-github-username>/my-first-blog.git -> git push -u origin HEAD

everytime you make changes that affect data model you do python manage.py makemigrations and then ,python manage.py migrate   



clear data in sqlite: 
Simply run the command

python manage.py flush
And answer the following question with 'yes'

This will IRREVERSIBLY DESTROY all data currently in the "qaapp" database,
and return each table to an empty state.
Are you sure you want to do this?

    Type 'yes' to continue, or 'no' to cancel: yes