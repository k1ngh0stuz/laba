from users import users
def get_user_info(user_id):
    user = users.get(user_id)
    if user is None:
        return f"Пользователь с id {user_id} не найден"
    return (
        f"Имя: {user['name']}\n"
        f"Возраст: {user['age']}\n"
        f"Телефон: {user['phone']}\n"
        f"Почта: {user['email']}"
    )


if __name__ == "__main__":
    try:
        uid = int(input("Введите id пользователя: "))
        print(get_user_info(uid))
    except ValueError:
        print("Нужно ввести число")