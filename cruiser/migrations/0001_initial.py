# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Registrant'
        db.create_table(u'cruiser_registrant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('experience', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('institution', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'cruiser', ['Registrant'])


    def backwards(self, orm):
        # Deleting model 'Registrant'
        db.delete_table(u'cruiser_registrant')


    models = {
        u'cruiser.registrant': {
            'Meta': {'object_name': 'Registrant'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'experience': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['cruiser']