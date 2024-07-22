usergroup = [{"first_name":"Helen", "age":13},{"first_name":"Buck", "age":19},{"first_name":"anni", "age":23}]

def get_user_name(user):
	return user['first_name'].lower()

def get_sorted_dict(users):
	if not isinstance(users,list):
		raise ValueError("not a list")
	if not len(users):
		raise ValueError("empty list")
	users_by_name = sorted(users, key=get_user_name)
	return users_by_name

print(get_sorted_dict(usergroup))
