#this file will handle CRUD operations
from flask import Blueprint, render_template, url_for
from flask_login import login_required, current_user

#first init the main file as part of flask app
main = Blueprint('main', __name__)
#blueprint way to org files in flask all function will be accessed
#thru blueprint thru main i.e. main.index, etc

#need decorator for all flask functions
#overwrites functionality for app

@main.route('/')
def index(): 
    return render_template('index.html')

@main.route('/profile')
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/all')
def all_baskets():
    user = User.query.filer_by(email=current_user.email).first()
    posts = user.posts
    return render_template('all_baskets.html', user=user, posts=posts)

@main.route('/new')
def new_basket():
    return render_template('create_basket.html')

@main.route('/new', methods=['POST'])
def new_basket_post():
    last_name = request.form.get('last_name')
    total_members = request.form.get('total_family_members')
    adults = request.form.get('adults')
    kids = request.form.get('adolescents')
    location = request.form.get('location')
    needs = request.form.get('needs')
    comments = request.form.get('comments')

    post = Post(last_name=last_name, total_members=total_members, adults=adults, kids=kids, location=location, needs=needs, comments=comments)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been added')
        return redirect(url_for('main.index'))

@main.route('/post/<int:post_id>/update', methods=['GET','POST'])
def update_post(post_id):
    post = Post.query.get_or_404(workout_id)
     if request.method == "POST":
        post.last_name = request.form['last_name']
        post.total_members = request.form['total_family_members']
        post.adults = request.form['adults']
        post.kids = request.form['kids']
        post.location = request.form['location']
        post.needs = request.form['needs']
        post.comments = request.form['comments']
     
        db.session.commit()
        flash('Your basket has been updated!')
        return redirect(url_for('main.user_posts'))

    return render_template('update_post.html', post=post)

@main.route('/post/<int:post_id>/delete', methods=['GET','POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(workout_id)
    db.session.delete(workout)
    db.session.commit()
    flash('Basket has been deleted!')
    return redirect(url_for('main.user_posts'))

@main.route('/about')
def about():
    return render_template('about.html')
