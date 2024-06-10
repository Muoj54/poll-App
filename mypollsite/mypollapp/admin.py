from django.utils import timezone
from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4  # Number of extra choice fields to display

class QuestionAdmin(admin.ModelAdmin):
    
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    def was_published_recently(self, obj):
        now = timezone.now()
        return obj.pub_date <= now <= now - timezone.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
# Register your models here.
admin.site.register(Question, QuestionAdmin)
# Register your models here.