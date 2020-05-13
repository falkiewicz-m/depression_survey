from django import forms
from .models import QuestionM, ChoiceM, Current_answer

class rhSurvey1(forms.Form):
    answers_1 = forms.ChoiceField(widget=forms.RadioSelect, choices=[], required=True)
    answers_2 = forms.ChoiceField(widget=forms.RadioSelect, choices=[], required=True)
    answers_3 = forms.ChoiceField(widget=forms.RadioSelect, choices=[], required=True)
    answers_4 = forms.ChoiceField(widget=forms.RadioSelect, choices=[], required=True)
    answers_5 = forms.ChoiceField(widget=forms.RadioSelect, choices=[], required=True)
    answers_6 = forms.ChoiceField(widget=forms.RadioSelect, choices=[], required=True)
    answers_7 = forms.ChoiceField(widget=forms.RadioSelect, choices=[], required=True)
    answers_8 = forms.ChoiceField(widget=forms.RadioSelect, choices=[], required=True)
    answers_9 = forms.ChoiceField(widget=forms.RadioSelect, choices=[], required=True)
    answers_10 = forms.ChoiceField(widget=forms.RadioSelect, choices=[], required=True)
    answers_11 = forms.ChoiceField(widget=forms.RadioSelect, choices=[], required=True)
    answers_12 = forms.ChoiceField(widget=forms.RadioSelect, choices=[], required=True)
    answers_13 = forms.ChoiceField(widget=forms.RadioSelect, choices=[], required=True)
    answers_14 = forms.ChoiceField(widget=forms.RadioSelect, choices=[], required=True)
    answers_15 = forms.ChoiceField(widget=forms.RadioSelect, choices=[], required=True)
    answers_16 = forms.ChoiceField(widget=forms.RadioSelect, choices=[], required=True)
    answers_17 = forms.ChoiceField(widget=forms.RadioSelect, choices=[], required=True)
    answers_18 = forms.ChoiceField(widget=forms.RadioSelect, choices=[], required=True)
    answers_19 = forms.ChoiceField(widget=forms.RadioSelect, choices=[], required=True)
    answers_20 = forms.ChoiceField(widget=forms.RadioSelect, choices=[], required=True)



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        get1 = ChoiceM.objects.filter(question_fk=1).values_list('choice_text', flat=True)
        self.fields['answers_1'].choices = [(choice_text, choice_text) for choice_text in get1]
        self.fields['answers_1'].label= QuestionM.objects.filter(pk=1).values_list('question_text', flat=True)[0]

        get2 = ChoiceM.objects.filter(question_fk=2).values_list('choice_text', flat=True)
        self.fields['answers_2'].choices = [(choice_text, choice_text) for choice_text in get2]
        self.fields['answers_2'].label= QuestionM.objects.filter(pk=2).values_list('question_text', flat=True)[0]

        get3 = ChoiceM.objects.filter(question_fk=3).values_list('choice_text', flat=True)
        self.fields['answers_3'].choices = [(choice_text, choice_text) for choice_text in get3]
        self.fields['answers_3'].label= QuestionM.objects.filter(pk=3).values_list('question_text', flat=True)[0]

        get4 = ChoiceM.objects.filter(question_fk=4).values_list('choice_text', flat=True)
        self.fields['answers_4'].choices = [(choice_text, choice_text) for choice_text in get4]
        self.fields['answers_4'].label= QuestionM.objects.filter(pk=4).values_list('question_text', flat=True)[0]

        get5 = ChoiceM.objects.filter(question_fk=5).values_list('choice_text', flat=True)
        self.fields['answers_5'].choices = [(choice_text, choice_text) for choice_text in get5]
        self.fields['answers_5'].label= QuestionM.objects.filter(pk=5).values_list('question_text', flat=True)[0]

        get6 = ChoiceM.objects.filter(question_fk=6).values_list('choice_text', flat=True)
        self.fields['answers_6'].choices = [(choice_text, choice_text) for choice_text in get6]
        self.fields['answers_6'].label= QuestionM.objects.filter(pk=6).values_list('question_text', flat=True)[0]

        get7 = ChoiceM.objects.filter(question_fk=7).values_list('choice_text', flat=True)
        self.fields['answers_7'].choices = [(choice_text, choice_text) for choice_text in get7]
        self.fields['answers_7'].label= QuestionM.objects.filter(pk=7).values_list('question_text', flat=True)[0]

        get8 = ChoiceM.objects.filter(question_fk=8).values_list('choice_text', flat=True)
        self.fields['answers_8'].choices = [(choice_text, choice_text) for choice_text in get8]
        self.fields['answers_8'].label= QuestionM.objects.filter(pk=8).values_list('question_text', flat=True)[0]

        get9 = ChoiceM.objects.filter(question_fk=9).values_list('choice_text', flat=True)
        self.fields['answers_9'].choices = [(choice_text, choice_text) for choice_text in get9]
        self.fields['answers_9'].label= QuestionM.objects.filter(pk=9).values_list('question_text', flat=True)[0]

        get10 = ChoiceM.objects.filter(question_fk=10).values_list('choice_text', flat=True)
        self.fields['answers_10'].choices = [(choice_text, choice_text) for choice_text in get10]
        self.fields['answers_10'].label= QuestionM.objects.filter(pk=10).values_list('question_text', flat=True)[0]

        get11 = ChoiceM.objects.filter(question_fk=11).values_list('choice_text', flat=True)
        self.fields['answers_11'].choices = [(choice_text, choice_text) for choice_text in get11]
        self.fields['answers_11'].label= QuestionM.objects.filter(pk=11).values_list('question_text', flat=True)[0]

        get12 = ChoiceM.objects.filter(question_fk=12).values_list('choice_text', flat=True)
        self.fields['answers_12'].choices = [(choice_text, choice_text) for choice_text in get12]
        self.fields['answers_12'].label= QuestionM.objects.filter(pk=12).values_list('question_text', flat=True)[0]

        get13 = ChoiceM.objects.filter(question_fk=13).values_list('choice_text', flat=True)
        self.fields['answers_13'].choices = [(choice_text, choice_text) for choice_text in get13]
        self.fields['answers_13'].label= QuestionM.objects.filter(pk=13).values_list('question_text', flat=True)[0]

        get14 = ChoiceM.objects.filter(question_fk=14).values_list('choice_text', flat=True)
        self.fields['answers_14'].choices = [(choice_text, choice_text) for choice_text in get14]
        self.fields['answers_14'].label= QuestionM.objects.filter(pk=14).values_list('question_text', flat=True)[0]

        get15 = ChoiceM.objects.filter(question_fk=15).values_list('choice_text', flat=True)
        self.fields['answers_15'].choices = [(choice_text, choice_text) for choice_text in get15]
        self.fields['answers_15'].label= QuestionM.objects.filter(pk=15).values_list('question_text', flat=True)[0]

        get16 = ChoiceM.objects.filter(question_fk=16).values_list('choice_text', flat=True)
        self.fields['answers_16'].choices = [(choice_text, choice_text) for choice_text in get16]
        self.fields['answers_16'].label= QuestionM.objects.filter(pk=16).values_list('question_text', flat=True)[0]

        get17 = ChoiceM.objects.filter(question_fk=17).values_list('choice_text', flat=True)
        self.fields['answers_17'].choices = [(choice_text, choice_text) for choice_text in get17]
        self.fields['answers_17'].label= QuestionM.objects.filter(pk=17).values_list('question_text', flat=True)[0]

        get18 = ChoiceM.objects.filter(question_fk=18).values_list('choice_text', flat=True)
        self.fields['answers_18'].choices = [(choice_text, choice_text) for choice_text in get18]
        self.fields['answers_18'].label= QuestionM.objects.filter(pk=18).values_list('question_text', flat=True)[0]

        get19 = ChoiceM.objects.filter(question_fk=19).values_list('choice_text', flat=True)
        self.fields['answers_19'].choices = [(choice_text, choice_text) for choice_text in get19]
        self.fields['answers_19'].label= QuestionM.objects.filter(pk=19).values_list('question_text', flat=True)[0]

        get20 = ChoiceM.objects.filter(question_fk=20).values_list('choice_text', flat=True)
        self.fields['answers_20'].choices = [(choice_text, choice_text) for choice_text in get20]
self.fields['answers_20'].label= QuestionM.objects.filter(pk=20).values_list('question_text', flat=True)[0]