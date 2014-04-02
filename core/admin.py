from django.contrib import admin
from core.models import Post, Comment, HomePageTitle, BannerImages, ClassStandard, AllQuestion


class HomePageTitleAdmin(admin.ModelAdmin):
    search_fields = ["title"]



class ClassStandardAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display  = ["title", "content", "image", "image_title", "image_alt_text", "image_description"]


class BannerImagesAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display  = ["title", "image_alt_text", "image_description", "image_caption"]
 
class AllQuestionAdmin(admin.ModelAdmin):
    search_fields = ["question"]
    list_display  = ["question", "option1", "option2", "option3", "classquestion"]
 

class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    display_fields = ["post", "author", "created"]

admin.site.register(Comment, CommentAdmin)
admin.site.register(HomePageTitle, HomePageTitleAdmin)
admin.site.register(BannerImages, BannerImagesAdmin)
admin.site.register(ClassStandard, ClassStandardAdmin)
admin.site.register(AllQuestion, AllQuestionAdmin)


