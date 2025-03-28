def greet_user(name):
    """
    接收用户名字并返回问候语
    """
    return f"Hello, {name}!"

if __name__ == "__main__":
    user_name = input("请输入你的名字: ")
    print(greet_user(user_name))