set up venv : 
1 : python3 -m venv myvenv      
2 : myvenv\Scripts\activate

start a project : 
1: cd to clbackend 
2: make sure you are in venv and type python maange.py starapp api <- this create api folder


django use so called ORM (object relational mapping )
views handles sql 
urls handle interaction between frontend and backend

sign in to git -> git init -> git config --global user.name "Your Name" , git config --global user.email you@example.com
git status -> git chekcout -> git add all . -> git status -> git commit -m "My Django Girls app, first commit" 
-> git remote add origin https://github.com/<your-github-username>/my-first-blog.git -> git push -u origin HEAD

everytime you make changes that affect data model you do python manage.py makemigrations and then ,python manage.py migrate   