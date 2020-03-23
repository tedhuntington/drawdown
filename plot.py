import matplotlib.pyplot as plt
import datetime as dt


def crashes(data, symbol):
    strs = {
        '^DJI': {
            'title': 'Current DJI sell off against major ones',
            'xlabel': ' # of trading days',
        },
        '^GSPC': {
            'title': 'Current S&P 500 sell off against major ones',
            'xlabel': '  # of trading days since first fall\nSince 1927\nUpdated at {}\n\nTwitter @resendedaniel_',
        }
    }

    color_max = '#E6550D'
    color_non_max = 'grey'
    ath = data['value'].max()
    #print(str(ath)) 

    fig, ax = plt.subplots(figsize=(10, 5))
    for x in data['cummax'].unique():
        #print(str(x))
        sub = data[data['cummax'] == x]
        #print(str(sub['d'].values[0]))
        #if sub['delta'].min() < -.02:
        if sub['delta'].min() < -.3:  #at least 10% loss
            plt.plot(sub['ord_d'], sub['delta'],
                     color=color_max if x == ath else color_non_max,
                     alpha=1 if x == ath else (sub['delta'].min() * -1) ** .8)
            plt.scatter(sub['ord_d'].max(),
                        sub['delta'].values[-1],
                        color=color_max if x == ath else color_non_max,
                        alpha=1 if x == ath else (sub['delta'].min() * -1) ** .8,
                        marker='.')
        #if sub['delta'].min() < -.2 or x == ath:
        #if x == ath:
            plt.text(sub['ord_d'].max(),
                     sub['delta'].values[-1],
                     ' {}: {:.1%} '.format(str(sub['d'].values[0])[:4], sub['delta'].values[-1]),
                     color=color_max if x == ath else color_non_max,
                     horizontalalignment='left' if str(sub['d'].values[0])[:4] in [
                '2018', '2004'] else 'right',
                verticalalignment='center')
            #print(str(sub['d'].values[0]))  #date
            #print(str(sub['delta'].min()))  #percent down from high
            #print(str(ath))  
            #print(str(x))  


    ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True)
    plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=True)
    plt.title(strs[symbol]['title'], size=28)
    plt.gca().set_yticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_yticks()])
    now = (dt.datetime.today() - dt.timedelta(days=0)).strftime('%Y-%m-%d')
    plt.xlabel('{}'.format(strs[symbol]['xlabel'].format(now)), horizontalalignment='right', x=1.0)

    plt.show()


def drawdown(data, symbol):
    fig, ax = plt.subplots(figsize=(10, 5))
    plt.plot(data['d'], data['drawdown'])
    ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True)
    plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=True)
    plt.gca().set_yticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_yticks()])
    plt.title('{} Drawdown'.format(symbol))
    plt.show()
