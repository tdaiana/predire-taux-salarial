from flask import render_template
from flask import flash

from werkzeug.utils import redirect

from app_demandes import app
from app_demandes.forms import SalaireForm

import numpy as np


# import pickle
# with open("param.pkl", "rb") as fh:
#     saved_model = pickle.load(fh)

@app.route('/')
@app.route('/index')
def index():
    projets = {'titre': 'A62'}
    return render_template('index.html', title='Accueil', mod=projets)


@app.route('/form_projet_input', methods=['GET', 'POST'])
def form_projet_input():
    projet_form = SalaireForm()

    if projet_form.validate_on_submit():
        flash('Profession: {}, Groupe: {}, Genre: {}, Type emploi: {}, Region: {}'.format(
            projet_form.profession.data,
            projet_form.groupe.data,
            projet_form.genre.data,
            projet_form.type_emploi.data,
            projet_form.region.data,
            # saved_model.predict([[projet_form.tv.data, projet_form.radio.data, projet_form.newspaper.data]])
        ))
        return redirect('/index')

    return render_template('form_projet_input.html',
                           title='Edition projet', form=projet_form)
