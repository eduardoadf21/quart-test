@bp.route('/cadastro', methods=('POST','GET'))
def register_user():
    if request.method == 'POST':
        username = request.form['username']
        fullname = request.form['fullname']
        email = request.form['email']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not fullname:
            error = 'Fullname is required.'
        elif not email:
            error = 'Email is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            repo.insert_user(username,fullname,email,password)
            return redirect(url_for("register.users"))
        else:
            flash(error)

    return render_template('register.html')
