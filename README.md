# streamlit_app_on_heroku
## heroku Deployment

### heroku is PaaS Archhitecture
______________________________________
Along with your applicatio files you need to take care of below mentioned steps
1. you need all the below mentioned files for deployment:
- requirements.txt
- Procfile
- setup.sh(you need setup.sh only for Streamlit)
- runtime.txt
2. Autodect the app type
3. git push & start running

---------------------------------------------

Create a Python VirtualEnv
(on command promt)

1. pip list(to see what are dependency are install)
2. python -m venv my_venv/
3. .\venv\Scripts\activate

- install some packages in virtualenv: sklearn, streamlit

- create requirment.txt file using below mentioned command:
- pip freeze > requirements.txt

------------------------------------------------------
- This part id required for NLP projects

- import nltk
- nltk.download('stopwords')
- nltk.download('wordnet')

------------------------------------------------------
- Install Heroku CLI and git CLI

- heroko login

- create a git repo and commit it locally; -  git init .
- git add .
- git commit -m "commit"
- heroku git remote - a app_name
- git push heroku master

------------------------------------------------------
- Run 
< heroku run bash -a app_name
> heroku run bash -a app_name

- Stop
- heroku ps:scale web=0 -a app_name
