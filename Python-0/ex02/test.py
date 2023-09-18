from find_ft_type import all_thing_is_obj

ft_tup = tuple("42")


all_thing_is_obj(["42", "yeah"])
all_thing_is_obj(ft_tup)
all_thing_is_obj({"42", "yeah"})
all_thing_is_obj({"42": "ueah"})
all_thing_is_obj("42")
