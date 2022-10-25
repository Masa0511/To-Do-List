from django import template

register = template.Library() # Djangoのテンプレートタグライブラリ

#超過日数の計算
@register.filter
def after_deadline(today, task):
    td = today - task.deadline
    return td.days
    
#残り日数の計算
@register.filter
def days_remaining(task, today):
    td = task.deadline - today
    return td.days
