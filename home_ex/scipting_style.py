import matplotlib.pyplot as plt

# 스타일 설정 (Set Style)
plt.style.use('ggplot')

x = [1,2,3,4,5]
y = [2,3,5,7,11]

plt.plot(x,y)

plt.title('Styled Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()
