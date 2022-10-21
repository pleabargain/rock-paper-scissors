# CS = computer science
And science means that one experiment, if followed exactly, should produce the same results. Right? Let's see!

# fork this project
https://github.com/pleabargain/rock-paper-scissors

I ran ```uvicorn main:app --reload```

and got 

http://127.0.0.1:8000/

it worked... moving on to create new poject on deta (see the docs on deta!)

And got a new URL
* https://xlr9we.deta.dev/
It works! :)

Let's test the docs:
* https://xlr9we.deta.dev/docs
They work too!

Let's test the game:
* https://xlr9we.deta.dev/shoot?weapon=paper
it worked as well!

I updated the class weapon with spock and lizard.

then I ran in CLI
```deta deploy```

Cloned an app and got it working on the web in less than 5 minutes. Very impressive! Now let's update the app by adding another 'weapon'.





# original readme below
# Rock Paper Scissors
A REST API built with Python [fastapi](https://fastapi.tiangolo.com/) and deployed with [Deta](https://www.deta.sh/). 
See it in action at [https://rockpaperscissors.deta.dev/docs](https://rockpaperscissors.deta.dev/docs).

See the corresponding explainer blog post about how this was built [here](https://www.gormanalysis.com/blog/building-and-deploying-rock-paper-scissors-with-python-fastapi-and-deta/).