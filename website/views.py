from types import NoneType
from flask import Blueprint, redirect, render_template, request, flash, jsonify, url_for
from flask_login import login_required, current_user
from sqlalchemy import null
from .models import Money
from . import db
import json
import requests
from forex_python.converter import CurrencyRates

views = Blueprint('views', __name__)

#Strona główna aplikacji, wyświetlenie portfela, podział na gotówkę oraz kartę
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        
        try:
            selectedValue = request.form['payment']
            if selectedValue == None: raise ValueError #sprawdzenie czy dokonano wyboru

            #przekierowanie do odpowiedniej strony po wybraniu jednej z opcji
            if(selectedValue == 'cash'):
                saldo = round(count_balance(cash_or_bank='cash'), 2)
                return render_template('cash.html', user=current_user, saldo=saldo)
            elif(selectedValue == 'card'):
                saldo = round(count_balance(cash_or_bank='card'), 2)
                return render_template("card.html", user=current_user, saldo=saldo)
        except:
            flash('Choose option!', category='error') #jeśli nie wybrano żadnej opcji pojawia się komunikat, że należy ją wybrać

    return render_template("home.html", user=current_user)

#Obliczenia salda dla gotówki oraz karty
def count_saldo(cash_or_bank = null, income_or_spending = null, name = null, date = null, currency=null):
    saldo = 0
    for money in current_user.money:
        if money.cash_or_bank == cash_or_bank:
            if money.cost != None:
                saldo += float(money.cost)

    return saldo

#Obliczenia salda dla wielu parametrów, żaden z paremtrów nie jest obowiązkowy, dlatego dla każdego sprawdzam czy jest nullem
def count_balance(cash_or_bank = null, income_or_spending = null, name = null, date = null, currency=null):
    saldo = 0
    list_money = []
    for money in current_user.money:
        if name == null:
            if currency == null:
                if cash_or_bank == null:
                    if income_or_spending == null:
                        if date == null:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                        elif money.date >= date:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                    elif(money.income_or_spending == income_or_spending):
                        if date == null:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                        elif money.date >= date:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                elif(money.cash_or_bank == cash_or_bank):
                    if income_or_spending == null:
                        if date == null:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                        elif money.date >= date:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                    elif(money.income_or_spending == income_or_spending):
                        if date == null:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                        elif money.date >= date:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
            elif(money.currency == currency):
                if cash_or_bank == null:
                    if income_or_spending == null:
                        if date == null:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                        elif money.date >= date:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                    elif(money.income_or_spending == income_or_spending):
                        if date == null:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                        elif money.date >= date:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                elif(money.cash_or_bank == cash_or_bank):
                    if income_or_spending == null:
                        if date == null:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                        elif money.date >= date:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                    elif(money.income_or_spending == income_or_spending):
                        if date == null:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                        elif money.date >= date:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add

        elif(money.name == name):
            if currency == null:
                if cash_or_bank == null:
                    if income_or_spending == null:
                        if date == null:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                        elif money.date >= date:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                    elif(money.income_or_spending == income_or_spending):
                        if date == null:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                        elif money.date >= date:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                elif(money.cash_or_bank == cash_or_bank):
                    if income_or_spending == null:
                        if date == null:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                        elif money.date >= date:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                    elif(money.income_or_spending == income_or_spending):
                        if date == null:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                        elif money.date >= date:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
            elif(money.currency == currency):
                if cash_or_bank == null:
                    if income_or_spending == null:
                        if date == null:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                        elif money.date >= date:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                    elif(money.income_or_spending == income_or_spending):
                        if date == null:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                        elif money.date >= date:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                elif(money.cash_or_bank == cash_or_bank):
                    if income_or_spending == null:
                        if date == null:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                        elif money.date >= date:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                    elif(money.income_or_spending == income_or_spending):
                        if date == null:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add
                        elif money.date >= date:
                            add = calculate_currency(money.currency, 'PLN', money.cost)
                            saldo += add

    return saldo

#Dodanie przychodu
@views.route('/add_income', methods=['GET', 'POST'])
@login_required
def add_income():
    if request.method == 'POST':
        
        try:
            name = request.form.get('name') 
            if name == None: raise ValueError #sprawdzenie czy wszystkie potrzebne pola zostały uzupełnione
            amount = request.form.get('amount')
            if amount == None: raise ValueError
            currency = request.form.get('currency')
            if currency == None: raise ValueError
            selectedValue = request.form['payment']
            if selectedValue == None: raise ValueError

            #dodanie wpisu do bazy danych odnośnie nowego przychodu
            new_income = Money(income_or_spending='income', name=name, cost=amount, user_id=current_user.id, cash_or_bank=selectedValue, currency=currency)
            db.session.add(new_income)
            db.session.commit()
            flash('Income successfully added!', category='success') #po dodaniu wpisu, pojawia się komunikat potwierdzający dodanie

        except ValueError:
            flash('Please fill all fields!', category='error') #Jeśli jakieś pola nie są uzupełnione pojawia się komukat, że należy wpisać wszystkie
        except:
            flash('Please fill all fields!', category='error')

    return render_template("add_income.html", user=current_user, currency_names=get_currency())

#Obliczanie salda 
@views.route('/balance', methods=['GET', 'POST'])
@login_required
def balance():
    type = null
    n = null
    balance = 0
    list_money = list()
    payment=null
    currency = null
    name = null
    if request.method == 'POST':
        try:
            type = request.form.get('type')
            if type == None:  type = null
            payment = request.form.get('payment')
            if payment == None: payment = null
            currency = request.form.get('currency')
            if currency == None: currency = null
            name = request.form.get('name')
            if name == None: raise ValueError
            balance = round(count_balance(income_or_spending = type, cash_or_bank=payment, name=name, currency=currency), 2)
        except ValueError:
            flash('Enter name!', category='error')
        except:
            flash('Enter name!', category='error')

    return render_template("balance.html", user=current_user,currency_names=get_currency(),type=type, balance=balance, payment=payment, currency=currency, name=name, list_money=list_money)
    

#Kalkulator walut
@views.route('/currency_converter', methods=['GET', 'POST'])
@login_required
def currency_converter():
    #wartości początkowe
    amount = 0
    currency_1 = 'EUR'
    currency_2 = 'PLN'
    converted = 0

    if request.method == 'POST':
       
        try: 
            currency_1 = request.form.get('currency_1') 
            if currency_1 == None: raise ValueError
            currency_2 = request.form.get('currency_2')
            if currency_2 == None: raise ValueError
            amount = float(request.form.get('amount')) #sprawdzenie czy wszystkie potrzebne pola są wypełnione
            if amount == None: raise ValueError

            converted = round(calculate_currency(currency_1, currency_2, amount), 2)
            flash('Convertred successfully', category='success')
        except:
            flash('Enter amount!', category='error')

    return render_template("currency_converter.html", user=current_user, currency_names=get_currency(), result=converted, amount=amount, curr_1=currency_1, curr_2=currency_2)

#metoda pobierająca wszystkie nazwy walut znajdujących się w CurrencyRates
def get_currency():
    c = CurrencyRates()
    currency_names = []
    currency_names.append('PLN')
    for currency in c.get_rates('PLN'):
        currency_names.append(currency)

    return currency_names

#metoda zwracająca przeliczoną walutę
def calculate_currency(currency_1, currency_2, amount):
    c = CurrencyRates()
    return c.convert(currency_1, currency_2, amount)

#Dodanie nowego wydatku
@views.route('/add_spending', methods=['GET', 'POST'])
@login_required
def add_spending():
    if request.method == 'POST':
        
        try:
            name = request.form.get('name') #sprawdzenie czy wszystkie potrzebne pola zostały uzupełnione
            if name == None: raise ValueError
            currency = request.form.get('currency')
            if currency == None: raise ValueError
            amount = (-1)*float(request.form.get('amount'))
            if amount == None: raise ValueError
            selectedValue = request.form['payment']
            if selectedValue == None: raise ValueError

            #dodanie wpisu o nowym wydatku do bazy danych 
            new_income = Money(income_or_spending='spending', name=name, cost=amount, user_id=current_user.id, cash_or_bank=selectedValue, currency=currency)
            db.session.add(new_income)
            db.session.commit()
            flash('Spending successfully added!', category='success') #jeśli wpis został poprawnie dodany, zostanie wyświetlony komunikat o pomyślnym dodaniu

        except ValueError:
            flash('Please fill all fields!', category='error') #jeśli jakieś pole jest nieuzupełnione, zostanie wyświetlony komunikat
        except:
            flash('Please fill all fields!', category='error')

    return render_template("add_spending.html", user=current_user, currency_names=get_currency())

@views.route('/cash', methods=['GET','POST'])
@login_required
def cash():
    return render_template("cash.html", user=current_user, saldo=count_saldo(cash_or_bank='cash'))

#Usuwanie wpisów
@views.route('/delete', methods=['POST'])
@login_required
def delete():
    money = json.loads(request.data)
    money_id = money['money_id']
    money = Money.query.get(money_id)
    if money:
        if money.user_id == current_user.id:
            db.session.delete(money)
            db.session.commit()

    return jsonify({})
