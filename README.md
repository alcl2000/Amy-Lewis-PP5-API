# Crack-It API

## Project description: 

‘Crack-it’ is a task management app. Designed to be as simple and easy to use as possible to make organising projects quick, easy, and fool-proof. The application consists of an API and a front-end React.js application. This is the documentation for the back-end API. 

[The front end repository can be found here](https://github.com/alcl2000/Amy-Lewis-PP5-FE)

## Entity Relationship diagram:

![A diagram showing the relationships between the user, profile, project and task models](assets/DRF_model_chart.jpg)

## Models and CRUD breakdown:


<table>
  <tr>
   <td>Model
   </td>
   <td>Endpoint(s)
   </td>
   <td>Create
   </td>
   <td>Retrieve
   </td>
   <td>Update
   </td>
   <td>Delete
   </td>
   <td>Filter
   </td>
   <td>Text search
   </td>
  </tr>
  <tr>
   <td>Users
   </td>
   <td>users/
<p>
users/:id/
   </td>
   <td>Yes
   </td>
   <td>Yes
   </td>
   <td>Yes
   </td>
   <td>No
   </td>
   <td>No
   </td>
   <td>No
   </td>
  </tr>
  <tr>
   <td>Profiles
   </td>
   <td>profiles/
<p>
profiles/:id/
   </td>
   <td>Yes (auto)
   </td>
   <td>Yes
   </td>
   <td>Yes
   </td>
   <td>No
   </td>
   <td>Projects, 
<p>
Tasks
   </td>
   <td>Username
   </td>
  </tr>
  <tr>
   <td>Projects
   </td>
   <td>projects/projects/:id
   </td>
   <td>Yes
   </td>
   <td>Yes
   </td>
   <td>Yes
   </td>
   <td>Yes
   </td>
   <td>Owner
   </td>
   <td>Title, 
<p>
Owner
   </td>
  </tr>
  <tr>
   <td>Tasks
   </td>
   <td>Tasks/tasks/:id
   </td>
   <td>Yes
   </td>
   <td>Yes
   </td>
   <td>Yes
   </td>
   <td>Yes
   </td>
   <td>Owner,
<p>
Important,
<p>
Project
   </td>
   <td>Owner, Important, 
<p>
Project
   </td>
  </tr>
</table>



## Backend - automated testing:

The automated tests for this project were written using pytest and the Django rest API’s custom ‘API test case’ the following tests were written and the app has 94% coverage according to htmlcov.



* Tasks Model: 
    * Users can retrieve task list
    * Logged in users can create tasks
    * Non logged in users can’t create tasks
    * Can retrieve task with valid id
    * Can’t retrieve a task with an invalid id
    * User can update own tasks
    * User can’t update others tasks
* Project Model:
    * Can retrieve project list
    * Logged in user can create projects
    * Non logged in user can't create projects
    * Can retrieve project with valid id
    * Can't retrieve project with invalid id
    * User can update own projects
    * User can’t update others projects
* Profile Model:
    * Users can retrieve profiles list
    * Profile created automatically with user
    *  User can retrieve profile with valid id
    * User can’t retrieve profile with invalid id
    * User can edit own profile
    * User can't edit others profiles

## Deployment Steps:



* Firstly, within your settings.py file:
* Make sure the dj-database-url and psycopg2 libraries are correctly installed
* Configure your dj-rest-auth library for JWTs
* Set ‘allowed hosts’ to the deployed app’s url
* Add a Procfile, to run the commands to correctly deploy your app
* Use the command ‘pip3 freeze > requirements.txt’ to create requirements file
* Go to Heroku.com and either sign in or create a new account
* From your dashboard click to create a new app
* Select a host in your region
* Once created: 
    * Collect the following variables from your env.py file:
        * Database URL
        * Cloudinary (or other cloud media hosting platform) URL
        * Secret Key
    * Add the following to the settings:
        * DISABLE_COLLECTSTATIC = 1
        * CLIENT_ORIGIN, with the url set to the deployed version of your front end app
        * CLIENT_ORIGIN_DEV, with the url set to the development url of your front end app
