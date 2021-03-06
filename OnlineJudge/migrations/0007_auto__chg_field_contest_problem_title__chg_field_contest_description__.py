# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Contest_Problem.title'
        db.alter_column('compile_contest_problem', 'title', self.gf('django.db.models.fields.TextField')(max_length=30))

        # Changing field 'Contest.description'
        db.alter_column('compile_contest', 'description', self.gf('django.db.models.fields.TextField')(max_length=400))

        # Changing field 'Contest.title'
        db.alter_column('compile_contest', 'title', self.gf('django.db.models.fields.TextField')(max_length=30))

    def backwards(self, orm):

        # Changing field 'Contest_Problem.title'
        db.alter_column('compile_contest_problem', 'title', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Contest.description'
        db.alter_column('compile_contest', 'description', self.gf('django.db.models.fields.TextField')(max_length=500))

        # Changing field 'Contest.title'
        db.alter_column('compile_contest', 'title', self.gf('django.db.models.fields.TextField')())

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_set'", 'to': "orm['auth.Group']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_set'", 'to': "orm['auth.Permission']", 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'compile.contest': {
            'Meta': {'object_name': 'Contest'},
            'contestor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '400'}),
            'endtime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'starttime': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {'max_length': '30'})
        },
        'compile.contest_problem': {
            'Meta': {'object_name': 'Contest_Problem'},
            'category': ('django.db.models.fields.TextField', [], {'blank': 'True', 'max_length': '20'}),
            'contest': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['compile.Contest']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_score': ('django.db.models.fields.IntegerField', [], {}),
            'problem': ('django.db.models.fields.TextField', [], {}),
            'testcase_in_1': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'testcase_in_2': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'testcase_in_3': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'testcase_out_1': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'testcase_out_2': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'testcase_out_3': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.TextField', [], {'max_length': '30'})
        },
        'compile.contest_submission': {
            'Meta': {'object_name': 'Contest_Submission', 'ordering': "['-created']"},
            'contest_problem': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['compile.Contest_Problem']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'fname': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'compile.submission_result': {
            'Meta': {'object_name': 'Submission_Result'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'result_type': ('django.db.models.fields.IntegerField', [], {}),
            'submission': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['compile.Contest_Submission']", 'unique': 'True'}),
            'testcase_passed': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'time_1': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'time_2': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'time_3': ('django.db.models.fields.FloatField', [], {'blank': 'True'})
        },
        'compile.submission_try': {
            'Meta': {'object_name': 'Submission_Try'},
            'finput': ('django.db.models.fields.files.FileField', [], {'blank': 'True', 'max_length': '100'}),
            'fname': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'object_name': 'ContentType', 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['compile']