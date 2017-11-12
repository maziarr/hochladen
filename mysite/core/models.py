from .formatchecker import ContentTypeRestrictedFileField
from django.db import models

class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = ContentTypeRestrictedFileField(upload_to='uploads/',
                                            content_types=['video/x-msvideo', 'application/pdf', 'video/mp4', 'audio/mpeg', ],
                                            max_upload_size=5242880,blank=True, null=True)

#    title = models.CharField(max_length=245)
#    handout = ContentTypeRestrictedFileField(upload_to='uploads/', content_types=['video/x-msvideo', 'application/pdf', 'video/mp4', 'audio/mpeg', ],max_upload_size=5242880,blank=True, null=True)





# class Stuff(models.Model):
#     title = models.CharField(max_length=245)
#     handout = ContentTypeRestrictedFileField(upload_to='uploads/', content_types=['video/x-msvideo', 'application/pdf', 'video/mp4', 'audio/mpeg', ],max_upload_size=5242880,blank=True, null=True)



# class MyApp(models.Model):
#     """ My application """
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=250)
#     file = ContentTypeRestrictedFileField(
#         upload_to='pdf',
#         content_types=['application/pdf', 'application/zip'],
#         max_upload_size=5242880
#     )
#     created = models.DateTimeField('created', auto_now_add=True)
#     modified = models.DateTimeField('modified', auto_now=True)
#
#     def __unicode__(self):
#         return self.name