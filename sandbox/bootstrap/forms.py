from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django.forms import ModelForm
from bootstrap.models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['pub_date', 'headline', 'content', 'reporter']
        
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_show_labels = False

        self.helper.add_input(Submit('submit', 'Submit'))