
import matplotlib.pyplot as plt

# funcion grafico de barra
def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()


# funcion grafico de pie
def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()


if __name__ == '__main__':
    
    labels = ['a', 'b', 'c']
    values = [20, 50, 30]
    generate_pie_chart(labels, values)