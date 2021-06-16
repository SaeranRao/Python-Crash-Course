alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print(f"Original position:{alien_0['x_position']}")
#向右边快速移动外星人。
#根据当前速度确定将外星人向右移动多远。
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#新位置为旧位置加上移动距离
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position:{alien_0['x_position']}")