unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

# 验证每个用户，知道没有未验证用户为止
# 将每个经过验证的用户都一到已验证用户列表中。
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user:{current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe fllowing users have been confirmed:")
for confirmed_user in confirmed_users:
    print(f"{confirmed_user.title()}")
