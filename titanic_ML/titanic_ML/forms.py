from django import forms

TICKET_CLASS_CHOICES= [('','--Choose--'),('1','1st Class'),('2','2nd Class'),('3','3rd Class')]
SEX_CHOICES = [('','--Choose--'),('0','Male'), ('1','Female')]
EMBARKED_CHOICES = [('','--Choose--'),('0','Southampton'), ('1','Cherbourg'),('2','Queenstown')]
TITLE_CHOICES = [('','--Choose--'),('0','Mr'),('1','Miss'),('2','Mrs'),('3','Master'),('4','Dr'),('5','Rev'),('6','Officer'),('7','Royalty')]

class TitanicForm(forms.Form):
    pclass = forms.ChoiceField(widget=forms.Select,choices=TICKET_CLASS_CHOICES, label='Ticket Class', required=True)
    sex = forms.ChoiceField(widget=forms.Select,choices=SEX_CHOICES, label='Sex', required=True)
    age = forms.IntegerField(max_value=120,min_value=0,label='Age',required=True)
    sibsp = forms.IntegerField(max_value=15,min_value=0,label='Siblings / Spouses',required=True)
    parch = forms.IntegerField(max_value=15,min_value=0,label='Parents / Children',required=True)
    fare = forms.IntegerField(max_value=512,min_value=0,label='Passenger fare',required=True)
    embarked = forms.ChoiceField(widget=forms.Select,choices=EMBARKED_CHOICES, label='Embarked', required=True )
    title = forms.ChoiceField(widget=forms.Select,choices=TITLE_CHOICES, label='Title', required=True)