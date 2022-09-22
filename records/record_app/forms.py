from .models import Mytable
from django import forms

class AddRecordsForm(forms.ModelForm):
    class Meta:
        model = Mytable
        fields = [
                'id',
                'title',
                'author',
                'editor',
                'year',
                'publisher',
                'source',
                'reference',
                'subject',
                'keywords',
                'abstarct',
                'loaction',
                'ref',
                'ref1',
                'published']


class RecordForm(forms.Form):
    title = forms.CharField(required=True, label='Title')
    author = forms.CharField(label='Author name')
    editor = forms.CharField(label='Editors')
    year = forms.IntegerField(label='year')
    publisher = forms.CharField(label='Publisher')
    source = forms.CharField(label='Source')
    reference = forms.CharField(label='References')
    subject = forms.CharField(label='Subject')
    keywords = forms.CharField(label='Keywords')
    abstarct = forms.CharField(label='Abstract')
    loaction = forms.CharField(label='Location')
    ref = forms.CharField(label='Ref')
    ref1 = forms.CharField(label='Ref1')
    published = forms.BooleanField()
    class Meta:
        fields = ["title", "author", "editor", "year", "publisher", "source", "references", "subject", "keywords", "abstarct", "loaction", "ref", "ref1", "published"]
        labels = {'title': "title", 'author': "author", 'editor': "editor", 'year': "year", 'publisher': "publisher", 'source': "source", 'references': "references", 'subject': "subject", 'keywords': "keywords", 'abstarct': "abstract", 'loaction': "location", 'ref': "ref", 'ref1': "ref1", 'published': "published"}
