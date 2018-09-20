Alayacare Data Engineering Test
===========================


### Test
This exercise will test your abilities to play with databases. You will be asked to create one, add some data to rows, insert rows, etc. The idea is to replicate some of the work you will be asked to do. We like to call the code we write reusable data hacks. Sometimes, we need to get creative to accomplish what is asked of us and this test will ask you to tip your toes in our world. Additionally, you will be asked to use git for version control and write some python.

We use pandas a lot when we deal with data.

Here's what you should install or have access to to complete this test:

* python
	- pandas
	- a library to access mariadb
* docker
* docker-compose
* a github account

### Installation
**/!\ You need to fork this repository. See [How to submit your work?](#how-to-submit-your-work)**

### Instructions

Please complete the following tasks.

When code is required, separate your commits by task and use the following format for your commit messages: TASK-{task number}: {meaningful message}

### Tasks
* TASK 1 (no commit): Use the sql file to create the database that you will use for this test. Use the `docker-compose.yml` file to launch an instance of `mariadb` and store the data there. Please note that `clients.idprofile` = `profiles.contact_id`.
* TASK 2: Write a sql query that gets all data from both table in one result set.
* TASK 3: Using `pandas`, get both tables separately and merge them in one `DataFrame`.
* TASK 3: On your copy of the profiles table, update the `value` column to 'fifth_row' (please don't write queries manually).
* TASK 4: Insert a new client and a new profile (use `sql`).
* TASK 5: Add a new column in the `profiles` table and fill it with random data.
* TASK 6: Implement a `python` class that you can instantiate with a username and password and that will expose a connection to your `mariadb` `docker` as a property.

Extra tasks:
- Write a test for your connector class.

### Documentation
This test uses 
* [Pandas](http://pandas.pydata.org/pandas-docs/stable/).
* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)

### How to submit your work?

1. ##### First you need to fork this repository.
2. ##### Then clone your fork locally.
3. ##### Once you've completed your work, you can submit a pull-request to the remote repository.
4. ##### Review your changes and validate.

And you're done!

More documentation on Github:
* https://help.github.com/articles/fork-a-repo/
* https://help.github.com/articles/using-pull-requests/
