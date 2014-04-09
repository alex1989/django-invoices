# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Invoice.invoicing_date'
        db.add_column(u'invoices_invoice', 'invoicing_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        for invoice in orm['invoices.Invoice'].objects.all():
            if invoice.confirmed:
                invoice.invoicing_date = invoice.created.date()
                invoice.save()

    def backwards(self, orm):
        # Deleting field 'Invoice.invoicing_date'
        db.delete_column(u'invoices_invoice', 'invoicing_date')


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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'invoices.invoice': {
            'Meta': {'ordering': "['-begins', '-ends']", 'object_name': 'Invoice'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '7', 'decimal_places': '2'}),
            'begins': ('django.db.models.fields.DateField', [], {}),
            'cancels': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'cancelled_by'", 'unique': 'True', 'null': 'True', 'to': u"orm['invoices.Invoice']"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'credit': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '7', 'decimal_places': '2'}),
            'credit_reason': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'default': "'EUR'", 'max_length': '3'}),
            'due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'ends': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoicing_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'is_paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'sequence_number': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'total_amount': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '7', 'decimal_places': '2'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'invoices'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'vat': ('django.db.models.fields.PositiveIntegerField', [], {'default': '19'}),
            'vat_amount': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '7', 'decimal_places': '2'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        },
        u'invoices.invoicesequencenumber': {
            'Meta': {'object_name': 'InvoiceSequenceNumber'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'invoices.item': {
            'Meta': {'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': u"orm['invoices.Invoice']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'total_amount': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '7', 'decimal_places': '2'})
        },
        u'invoices.lineitem': {
            'Meta': {'object_name': 'LineItem'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'line_items'", 'to': u"orm['invoices.Item']"}),
            'item_group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'line_items'", 'null': 'True', 'to': u"orm['invoices.LineItemGroup']"}),
            'timezone': ('django.db.models.fields.CharField', [], {'default': "'UTC'", 'max_length': '128'})
        },
        u'invoices.lineitemgroup': {
            'Meta': {'object_name': 'LineItemGroup'},
            'amount': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '7', 'decimal_places': '2'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'line_item_groups'", 'to': u"orm['invoices.Item']"}),
            'item_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'line_item_groups'", 'to': u"orm['invoices.LineItemType']"})
        },
        u'invoices.lineitemtype': {
            'Meta': {'object_name': 'LineItemType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        }
    }

    complete_apps = ['invoices']