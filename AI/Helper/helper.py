from IPython import display
import matplotlib.pyplot as plt

#plt.ion()

def plot(plot_list,plot_path, plot_name,title, y_axis, x_axis):
    #display.clear_output(wait=True)
    #display.display(plt.gcf())
    plt.clf()
    plt.title(title)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    #plt.plot(scores)
    ax = plt.subplot(1, 1, 1)
    i = len(plot_list)
    for plot in plot_list:
        [plot_data, plot_n] = plot
        ax.plot(plot_data, label = plot_n, zorder = i)
        ax.legend()
        i-= 1
    #plt.ylim(ymin=0)
    #plt.draw()
    #plt.text(len(scores)-1, scores[-1], str[scores[-1]])
    #plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.savefig(plot_path + plot_name)
