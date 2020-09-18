def from_queryset_to_list_of_tuples(queryset):
    return [item.to_tuple() for item in queryset]
