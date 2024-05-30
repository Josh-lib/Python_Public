import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [1000,200,304,456,900]
month = ["Jan", "Feb", "Mar", "Nay", "Apr"]
plt.xticks(x,month)
plt.plot(x,y)
plt.bar(x,y)
plt.ylabel("Sales in the UG")
plt.xlabel("Monthly")
plt.show()
