from django.contrib import admin

from .models import Question, Choice

# Register your models here.


# class QuestionAdmin(admin.ModelAdmin):
#     fields = ["pub_date", "question_text"]


# class ChoiceInLine(admin.StackedInline):
#     model = Choice
#     extra = 3


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    list_display = ("question_text", "pub_date", "was_published_recently")
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]})
    ]
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
