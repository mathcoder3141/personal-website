from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///entries.db'
db = SQLAlchemy(app)

class GuestBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='Unknown')
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog Post ' + str(self.id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/writings')
def writings():
    return render_template('writings.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/accomplishments')
def accomplishments():
    return render_template('/accomplishments.html')
    
@app.route('/guestbook', methods=['GET', 'POST'])
def entries():
    if request.method == 'POST':
        entry_content = request.form['content']
        entry_author = request.form['author']
        new_entry = GuestBook(content=entry_content, author=entry_author)
        db.session.add(new_entry)
        db.session.commit()
        return redirect('/guestbook')
    else:
        all_entries = GuestBook.query.order_by(GuestBook.created.desc()).all()
        return render_template('entries.html', posts=all_entries)

@app.route('/guestbook/new', methods=['GET', 'POST'])
def new_entry():
    if request.method == 'POST':
        post.author = request.form['author']
        post.content = request.form['content']
        new_post = GuestBook(content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/guestbook')
    else:
        return render_template('new_entry.html')

if __name__ == "__main__":
    app.run(debug=True)
