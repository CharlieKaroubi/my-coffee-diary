from flask import Blueprint, render_template, flash, request, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views',__name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    notes = Note.query.filter_by(user_id=current_user.id).all()
    
    if notes:
        # Sort notes by the integer value at the end of the 'data' attribute
        sorted_notes = sorted(notes, key=lambda note: int(note.data[-1]), reverse=True)
        return render_template("home.html", user=current_user, notes=sorted_notes)
    else:
        return render_template("home.html", user=current_user)


@views.route('/save_note', methods=['POST'])
def save_note():
    try:
        data = request.get_json()  # Get JSON data from the request
        if data is None:
            flash('No data received', category='error')
        
        note = data.get('note')
        if not note or len(note) < 1:
            flash('Shop name is too short', category='error')

        # Save to database
        new_note = Note(data=note, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()

        return jsonify({'message': 'Note added!', 'note': new_note.data}), 200
    except Exception as e:
        # Print the error to the console
        return jsonify({'message': 'Internal Server Error'}), 500


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/update-note', methods=['POST'])
def update_note():  
    note = json.loads(request.data) 
    noteId = note['noteId']
    rating = note['rating']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            updated_note = note.data[:-1]+str(rating)
            note.data = updated_note
            db.session.commit()
    
    return jsonify({})

@views.route('/view-card', methods = ['POST'])
def view_card():
    return render_template("cardview.html", user = current_user)