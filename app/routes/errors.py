from flask import render_template

from app.app import app


@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(403)
@app.errorhandler(500)
def general_error(*args, **kwargs):
    return render_template('error.html', errors=args)
