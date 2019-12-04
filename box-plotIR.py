import matplotlib.pyplot as plt
import glob


def norm(IR):
    normed = list()
    lo, hi = 99999., 0.

    for ir in IR:
        if ir < lo:
            lo = ir
        if ir > hi:
            hi = ir

    alpha = 1./(hi-lo)
    for ir in IR:
        normed.append(alpha*ir)
    
    return normed


def get_box_data(fns=[]):
    cut = lambda x: x[:-2]
    IR_data = []
    for fn in fns:
        with open(fn, 'r') as f:
            content = f.readlines()
        data = list(content)
        data_values = list(map(cut,data))
        IR = list(map(float,data_values))
        IR_data.append(IR)
    return IR_data


def get_indv_box_data():
    files = {'beethoven': '/home/jason/scripts/data/1-beethoven_box_plt_u.txt',
             'jarret': '/home/jason/scripts/data/2-jarrett-sunbear_box_plt_u.txt',
             'mehldau': '/home/jason/scripts/data/3-mehldau-10years_box_plt_u.txt',
             'beethoven-m': '/home/jason/scripts/data/beethoven-model_box_plt_u.txt',
             'chopin-m': '/home/jason/scripts/data/chopin-model_box_plt_u.txt',
             'classical-m': '/home/jason/scripts/data/classical-tiny_box_plt_u.txt',
             'liszt-m': '/home/jason/scripts/data/liszt-model_box_plt_u.txt',
             'mehldau-m': '/home/jason/scripts/data/mehldau-model_box_plt_u.txt',
             'mixed-m': '/home/jason/scripts/data/mixed-tiny_box_plt_u.txt',
             'tatum-m': '/home/jason/scripts/data/tatum-model_box_plt_u.txt',
             'tatum': '/home/jason/scripts/data/tatum-solo_box_plt_u.txt',
             'bach-m': '/home/jason/magenta-cf/magenta/magenta/music/stats/bach-model_box_plt_u.txt'
            }
    cut = lambda x: x[:-2]
    IR_data = {}
    for label, fn in files.items():
        with open(fn, 'r') as f:
            content = f.readlines()
        data = list(content)
        data_values = list(map(cut,data))
        IR = list(map(float,data_values))
        IR_data[label]= IR
    return IR_data


def sort_IR(IR_data):
    mean = lambda n: float(sum(n)) / max(len(n), 1)
    tuples = list(IR_data.items())
    return sorted(tuples, key=lambda x: mean(x[1]), reverse=True)


def main():    
    box_plot_data = get_indv_box_data()
    fig = plt.figure()
    # fig.suptitle('Ballsack',fontsize=14,fontweight='bold')
    ax = fig.add_subplot(111)
    # ax.boxplot(box_plot_data,patch_artist=True,
    #                 labels=['beethoven'])
    ax.set_title('Information Rates of models and composed music')
    ax.set_xlabel('Source')
    ax.set_ylabel('Information Rate')

    # boxes = [box_plot_data['beethoven'], box_plot_data['beethoven-m'],
    #          box_plot_data['tatum'], box_plot_data['tatum-m'],
    #          box_plot_data['mehldau'], box_plot_data['mehldau-m']]
    # labels = ['beethoven','beethoven-m','tatum','tatum-m','melhdau','mehldau-m']
    tuples = sort_IR(box_plot_data)
    boxes = [tup[1] for tup in tuples]
    labels = [tup[0] for tup in tuples]
    # print(boxes)
    print(labels)
    box = plt.boxplot(boxes,patch_artist=True,
                    labels=labels)
    colors = ['cyan','lightblue','orange','beige','turquoise','lightgreen','red','purple','darkblue','green','yellow']
    # colors = ['cyan', 'cyan', 'lightgreen', 'lightgreen', 'purple', 'purple']	
    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)

    plt.savefig('beethoven-IR.png', bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
	main()