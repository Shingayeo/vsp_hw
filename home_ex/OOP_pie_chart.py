import matplotlib.pyplot as plt

fig, ax = plt.subplots()

labels = ['A', 'B', 'C', 'D']
sizes = [20,30,25,25]

# 원형 차트 생성
ax.pie(sizes, labels=labels, autopct='%1.1f%%') # Axes 객체의 pie() 메소드 사용해 원형 차트 생성

ax.set_title('Pie Chart')

# 축 숨기기: 원형 차트는 보통 숨김
ax.axis('equal') # 원형 차트가 원형으로 보이도록 함

plt.show()
