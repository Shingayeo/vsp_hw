import matplotlib.pyplot as plt

fig, ax = plt.subplots()

categories = ['A', 'B', 'C', 'D' ]
values = [10,20,15,25]

# 막대 그래프 생성
ax.bar(categories, values) # Axes 객체의 bar() 메소드를 이용해 막대 그래프 생성

# 제목과 축 레이블 설정
ax.set_title('Bar Chart')
ax.set_xlabel('Categories')
ax.set_ylabel('Values')

# 그리드 추가
ax.grid(True, axis = 'x') # Y축에 그리드 추가

# 축 숨기기
ax.spines['top'] .set_visible(False)
ax.spines['right'] .set_visible(False)

plt.show()
