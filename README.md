# Speed Circuit

Ningg a NEEEEEEIIINNNGG a ning a ning!

Note to self: Use monoton font https://fonts.google.com/specimen/Monoton

## Development

0. Install required packages
    ``` bash
    $ easy_install pip
    $ pip install virtualenv
    ```

0. Setup and run
    ``` bash
    $ npm i
    $ source env/bin/activate
    $ python run.py
    ```

0. Starts at [localhost:5000](http://localhost:5000)

0. Webpack static assets watcher and bundler
    ``` bash
    $ npm run watch
    ```

0. Setup database
    ``` bash
    $ python manage.py db init
    $ python manage.py db migrate
    $ python manage.py db upgrade
    ```

0. Create a dude
    ``` bash
    $ python
    $ >>> from app.app import db
    $ >>> from app.models import User
    $ >>> user = User('joe', '123')
    $ >>> db.session.add(user)
    $ >>> db.session.commit()
    ```

0. Stop
    - Ctrl+C
    ``` bash
    $ deactivate
    ```
