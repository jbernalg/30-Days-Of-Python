
import matplotlib.pyplot as plt

# funcion grafico de barra
def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

