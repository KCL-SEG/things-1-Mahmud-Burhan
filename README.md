This leads to a page where you can accept an invitation to the exercise. Accepting this invitation will create a repository in your GitHub.com account. Find this new repository and open it. Then, find the URL of the repository on GitHub and clone it to your machine with:

$ git clone URL

where URL is the URL of your repository on GitHub. The repository includes a Django project without application, as well as some tests to evaluate your solution. You must not touch the tests that were provided. I recommend that you do not look at the tests initially to complete the exercises and also write your own model tests independently. You can read the test code if you really want to though.

Once your exercise is complete, you need to push your repository with:

$ git push

GitHub will automatically test your solution. Check that your solution has passed the tests. A partial solution (one that solves some but not all exercises), should pass some tests.
Assignment

The code provides a basic Django project. Before you can use it, you need to create a virtual environment and activate it. This is explained in video Practice 2.2. Then, install the packages required to be able to run the code with the command:

$ pip3 install -r requirements.txt

Exercise 1: Add app and home view

The first exercise involves creating an app and adding a view that renders a simple HTML page. You can do this exercise as soon as you have completed all videos up to Practice 2.5.

    Create an app called things in the project and ensure it is registered in the settings.py file.
    Extend the things app with a view that renders a simple HTML page. The HTML must include a title in the document head:

    <title>Things</title>

    and it must display a title on the page body:

    <h1>Things</h1>	

    Extend the project with a URL to the root path. This must lead to the view that you just created.

If you complete this exercise successfully and push it, your solution will pass the test called "Exercise 1: Add app and home view".
Exercise 2: Add a basic things model

In this exercise, you are expected to extend the things app with a basic model that contains a few attributes. You can do this exercise as soon as you have completed the videos up to Practice 2.8.

To complete this exercise, extend the application with a model called Thing. A Thing entity has the following three attributes:

    name: a short string that identifies a thing.
    description: a slightly longer string that describes a thing.
    quantity: an integer that identifies the number of items of a thing we possess.

Important: You should know that that this exercise requires you to create a class called Thing. Model classes must extend django.db.models.Model. Make sure that your model class does.

If you complete this exercise successfully and push it, your solution will pass the test called "Exercise 2: Add a basic things model".
Exercise 3: Refining the Thing model

In this exercise, you are expected to refine the Thing model. You can do this exercise as soon as you have completed the videos up to Practice 2.10.

To complete this exercise, your solution must enforce the following constraints:

    name must be unique, must not be blank, and must consist of 30 characters or less.
    description need not be unique, may be blank, and must consist of 120 characters of less.
    quantity need not be unique, and must be an integer value between 0 and 100 (inclusive). quantity may be 0 and it may be 100, but not less than 0 and not more than 100.

If you complete this exercise successfully and push it, your solution will pass the test called "Exercise 3: Refining the Thing model".
