# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ReportedUser.category'
        db.add_column(u'issues_reporteduser', 'category',
                      self.gf('django.db.models.fields.CharField')(default='NAP', max_length=3),
                      keep_default=False)

        # Adding field 'ReportedUser.note'
        db.add_column(u'issues_reporteduser', 'note',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'ReportedLink.category'
        db.add_column(u'issues_reportedlink', 'category',
                      self.gf('django.db.models.fields.CharField')(default='BKN', max_length=3),
                      keep_default=False)

        # Adding field 'ReportedLink.note'
        db.add_column(u'issues_reportedlink', 'note',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ReportedUser.category'
        db.delete_column(u'issues_reporteduser', 'category')

        # Deleting field 'ReportedUser.note'
        db.delete_column(u'issues_reporteduser', 'note')

        # Deleting field 'ReportedLink.category'
        db.delete_column(u'issues_reportedlink', 'category')

        # Deleting field 'ReportedLink.note'
        db.delete_column(u'issues_reportedlink', 'note')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'folder.folder': {
            'Meta': {'unique_together': "(('owner', 'name'),)", 'object_name': 'Folder'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'folders'", 'to': u"orm['maker.Maker']"})
        },
        u'issues.reportedlink': {
            'Meta': {'unique_together': "(('reporter', 'link'),)", 'object_name': 'ReportedLink'},
            'category': ('django.db.models.fields.CharField', [], {'default': "('BKN', 'Broken Link')", 'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'issues_reported'", 'to': u"orm['link.Link']"}),
            'note': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'reporter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'links_reported'", 'to': u"orm['maker.Maker']"})
        },
        u'issues.reporteduser': {
            'Meta': {'unique_together': "(('reporter', 'user'),)", 'object_name': 'ReportedUser'},
            'category': ('django.db.models.fields.CharField', [], {'default': "('NAP', 'Not Appropriate')", 'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'reporter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'users_reported'", 'to': u"orm['maker.Maker']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'issues_reported'", 'to': u"orm['maker.Maker']"})
        },
        u'link.link': {
            'Meta': {'object_name': 'Link'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'links'", 'null': 'True', 'to': u"orm['folder.Folder']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'links'", 'to': u"orm['maker.Maker']"}),
            'photo_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'maker.maker': {
            'Meta': {'object_name': 'Maker'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'photo_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'signup_type': ('django.db.models.fields.CharField', [], {'default': "'RG'", 'max_length': '2'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        }
    }

    complete_apps = ['issues']
