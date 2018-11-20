from django.contrib import admin
from .models import Category, Post, Moderator, NormalUser, Topic, Vote, VotePost, VoteTopic

class TopicInline(admin.TabularInline):
  model = Topic
  extra = 0

  def get_form(self, request, *args, **kwargs):
    form = super(CategoryAdmin, self).get_form(request, *args, **kwargs)
    form.base_fields['user'].initial = request.user
    return form
  
class CategoryAdmin(admin.ModelAdmin):
  fieldsets = [
    (None,               {'fields': ['title']}),
  ]
  inlines = [TopicInline]
  list_display = ('title',)
  search_fields = ['title']

class ModeratorAdmin(admin.ModelAdmin):
  ''

admin.site.register(Category, CategoryAdmin)
admin.site.register(Moderator, ModeratorAdmin)
admin.site.register(NormalUser)
