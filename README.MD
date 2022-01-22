## This is the PP4 Milestone Project, from Mark Peeters, for Code Institute.

### This is a Tech Blog Website build with Django and PostgreSQL."


# UX

## Goals

### Visitor Goals


The target audience to the Blog would be:
- Persons with affinity towards developments in the IT industry.
- IT engineers

### User Stories:
As a new User to this website, I want to:
* be able to signup to the Website
* be able to add posts to the website
* be able to easily add comments to the website
* be able to like posts
* be able to add categories

### Wireframes: 

TBD

## Features

### Layout


### Existing Features

#### Navigation Bar


#### The Register Page

#### The Login Page

#### The 'Show Profile' Page


### Features Left to Implement

## Main Technologies Used

### Languages used

* This project uses **HTML**, **CSS**, **JavaScript** and **Python** programming languages.

### Tools used

* **Balsamiq** to create the wireframes for this project. - to be added
* **Django** as python web framework rapid development and clean, pragmatic design.
* **Git** to handle version control.
* **GitHub** to store the project code remotely.
* **PIP** for installation of tools needed in this project.
* **Heroku** for deployment
* **Django ck-editor** to style django forms.

### Libraries utilised

* **Bootstrap 4** to simplify the structure of the website and make the website responsive easily.
* **jQuery**

## Databases

### Databases used

During development sqlite3 has been utilised on my local machine.
On deployment this has been deployed to a PostgreSQL database.


## Testing

TBD

### User Testing

#### Manual User testing:

### Below are the list of Internet Browsers that were used to test the display of the website:

### Below are the list of websites I used to test the HTML, CSS and JS code:

1. [W3C HTML Validator](https://validator.w3.org/) This is a HTML online validitor.
2. [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) This is a CSS online validitor.
3. [CSS Lint](http://csslint.net/) CSS Lint is an open source CSS code quality tool I used.

#### Meeting the needs of the user stories (as described in the UX section of this README file)

## Deployment

### Local Deployment

This project was developed using the Gitpod IDE, committed to git and pushed to GitHub using Git PUSH in Gitpod..

The GitHub Repository is here: https://github.com/Markp1312/PP4-Techblog_Django
The application is live here: https://pp4-marktechblog.herokuapp.com

```
### Heroku Deployment

To deploy this Blog to Heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to whichever is applicable for your location.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

`"SECRET_KEY": "enter your own value here",`
`"DATABASE_URL": "enter your own value here",`

8. In your heroku dashboard, click "Deploy". Scroll down to "Manual Deploy", select the master branch then click "Deploy Branch"
9. Once the build is complete, click on the "View app" button.

The app should open in a new tab.

## Credits

### Content


####Credits:
##### Code
1. John Elder - https://www.codemy.com
2. Code Institute - Think Before I Blog
3. Stackoverflow - https://www.stackoverflow.com


### Acknowledgements

- I'd like to thank my colleague Ahmed Qubia, for his excellent insights and usefull suggestions.

 
### Thank you.