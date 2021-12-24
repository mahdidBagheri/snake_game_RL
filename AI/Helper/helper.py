from IPython import display
import matplotlib.pyplot as plt

#plt.ion()

def plot(mean_scores, plot_name):
    #display.clear_output(wait=True)
    #display.display(plt.gcf())
    plt.clf()
    plt.title("Training...")
    plt.xlabel("N Games")
    plt.ylabel("Score")
    #plt.plot(scores)
    plt.plot(mean_scores)
    #plt.ylim(ymin=0)
    #plt.draw()
    #plt.text(len(scores)-1, scores[-1], str[scores[-1]])
    #plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.savefig(plot_name)
