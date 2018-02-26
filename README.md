# Speed Circuit

Ningg a NEEEEEEIIINNNGG a ning a ning!

## Development

0. Install required packages
    ``` bash
    $ easy_install pip
    $ pip install virtualenv
    ```

0. Setup and run
    ``` bash
    $ source env/bin/activate
    $ python run.py
    ```

0. Starts at [localhost:5000](http://localhost:5000)

0. Webpack static assets watcher
    ``` bash
    $ npm run watch
    ```

0. Setup database
    ``` bash
    $ python manage.py db init
    $ python manage.py db migrate
    $ python manage.py db upgrade
    ```

0. Stop
    - Ctrl+C
    ``` bash
    $ deactivate
    ```