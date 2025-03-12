from django.contrib import admin

from book_app.models import PublishingHouseAuthor, Author, PublishingHouse, Book


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')

    def has_change_permission(self, request, obj = None):
        return False

    def has_delete_permission(self, request, obj = None):
        return False

    def has_add_permission(self, request, obj = None):
        if request.user.is_superuser:
            return True
        return False

class PublicationAuthorInline(admin.TabularInline):
    model = PublishingHouseAuthor
    extra = 0

class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [PublicationAuthorInline,]

class BookAdmin(admin.ModelAdmin):
    list_display = ('isbn','title', 'author')
    exclude = ('user_created',)

    def save_model(self, request, obj, form, change):
        obj.user_created = request.user
        return super(BookAdmin, self).save_model(request, obj, form, change)


admin.site.register(Author,AuthorAdmin)
admin.site.register(PublishingHouse,PublishingHouseAdmin)
admin.site.register(Book,BookAdmin)