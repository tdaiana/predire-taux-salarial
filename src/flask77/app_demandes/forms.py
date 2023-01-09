from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, StringField
from wtforms.validators import DataRequired


class SalaireForm(FlaskForm):
    profession_choix = ["um", "doix", "tres"]
    profession = SelectField('Profession (CNP4)', choices=profession_choix, validators=[DataRequired()])

    groupe_choix = ["um", "doix", "tres"]
    groupe = SelectField("Groupe d'Age", choices=groupe_choix, validators=[DataRequired()])

    genre_choix = [(0, 'Femme'), (1, 'Homme')]
    genre = RadioField('Genre', choices=genre_choix, validators=[DataRequired()])

    type_choix = ["um", "doix", "tres"]
    type_emploi = SelectField("Type d'emploi", choices=type_choix, validators=[DataRequired()])

    region_choix = ['Québec', 'Non-Québec']
    region = SelectField('Region', choices=region_choix, validators=[DataRequired()])

    submit = SubmitField("Sauvegarder")
